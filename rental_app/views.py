from django.shortcuts import render, redirect 
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import logout 
from rental_app.forms import CarForm,DriverForm,BookingForm
from rental_app.models import Car,Driver,Booking
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Sum
from django.core.mail import send_mail
from confluent_kafka import Producer
from django.conf import settings

#from .kafka_producer import kafka_produce_event
from .kafka_producer import send_email_to_kafka
import json
from django.http import JsonResponse

# hdfs
from hdfs import InsecureClient

HDFS_URL = 'http://localhost:9870'
HDFS_USER = 'mun159323'
HDFS_DIR = '/uploads/'

# Create your views here.

def record_car(request):  
    if request.method == "POST":  
        form = CarForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                messages.success(request, "The car recorded successfully.") 
                return redirect('/home_page')    
            except:  
                pass  
    else:  
        form = CarForm()
        drivers = Driver.objects.all()   
    return render(request,'car_reg.html',{'form':form,'drivers':drivers})   

 
def record_driver(request):  
     
    if request.method == "POST":  
        form = DriverForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                messages.success(request, "Driver recorded successfully.") 
                return redirect('/home_page')  
            except:  
                pass  
    else:  
        form = DriverForm()  
    drivers = Driver.objects.all() 
    return render(request,'driver_reg.html',{'form':form,'drivers':drivers})  
def show_driver(request):  
    drivers = Driver.objects.all()  
    return render(request,"driver_view.html",{'drivers':drivers}) 
 
def edit_driver(request, id):  
    driver = Driver.objects.get(driver_id=id)  
    return render(request,'driver_edit.html', {'driver':driver})
  
def update_driver(request, id): 
    driver = Driver.objects.get(driver_id=id) 
    form = DriverForm(request.POST, instance = driver)  
    if form.is_valid():  
        form.save()   
    #drivers = Driver.objects.all() 
    #return render(request,'driver_reg.html',{'form':form,'drivers':drivers})
    messages.success(request, "Driver's information updated successfully.") 
    return redirect('/home_page') 
 
def destroy_driver(request, id): 
    driver = Driver.objects.get(driver_id=id)  
    driver.delete() 
    drivers = Driver.objects.all()  
    return redirect("/record_driver",{'drivers':drivers}) 



@login_required(login_url='/login/')  # Redirects to the login page if not logged in
def home_page(request): 
    #unbooked_cars = Car.objects.filter(Q(booking__isnull=True) | ~Q(booking__status='Booked')).distinct() # Cars that have no bookings.
    available_cars_list = Car.objects.filter(status='Available')
    booked_cars_list = Car.objects.filter(status='Booked')
    subscribers_list = User.objects.filter(is_superuser = False)
    total_income = Booking.objects.aggregate(total=Sum('total_cost'))['total']
    return render(request,'homePage.html', {'available_cars':available_cars_list.count(),'booked_cars':booked_cars_list.count(),'subscribers':subscribers_list.count(), 'total_income':total_income})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('login')

        try:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user.full_clean()  # Validates fields
            user.save()
            messages.success(request, "Account created successfully.")
            login(request, user)
            return redirect('login')       
        except ValidationError as e:
            messages.error(request, e)
        except Exception:
            messages.error(request, "Username already exists or invalid input.")
    
    return render(request, 'login.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in.")
            
            if request.user.is_superuser:
                #unbooked_cars = Car.objects.filter(Q(booking__isnull=True) | ~Q(booking__status='Booked')).distinct() # Cars that have no bookings.
                available_cars_list = Car.objects.filter(status='Available')
                booked_cars_list = Car.objects.filter(status='Booked')
                subscribers_list = User.objects.filter(is_superuser = False)
                total_income = Booking.objects.aggregate(total=Sum('total_cost'))['total']
                return render(request,'homePage.html',{'user':user,'available_cars':available_cars_list.count(),'booked_cars':booked_cars_list.count(),'subscribers':subscribers_list.count(), 'total_income':total_income})
            
            else:
                form = BookingForm()   
                cars_list = Car.objects.all()
                return render(request,'clientPage.html',{'form':form,'cars_list':cars_list,'user':user}) 
                #return redirect('booking')
            
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')


# Example of session data access
def example_view(request):
    if request.user.is_authenticated:
        #return render(request, 'dashboard.html')
        return redirect('record_driver')
    
    else:
        return redirect('login')

@login_required(login_url='/login/')  # Redirects to the login page if not logged in
def renting_view(request):
    form = BookingForm()   
    #unbooked_cars = Car.objects.filter(Q(booking__isnull=True) | ~Q(booking__status='Booked')).distinct()
    cars_list = Car.objects.all()
    return render(request,'clientPage.html',{'form':form,'cars_list':cars_list})

def upload_to_hdfs(file, file_name):
    client = InsecureClient(HDFS_URL, user=HDFS_USER)
    hdfs_path = f"{HDFS_DIR}{file_name}"
    with client.write(hdfs_path, overwrite=True) as writer:
        for chunk in file.chunks():
            writer.write(chunk)
    return hdfs_path

def create_booking(request):
    if request.method == 'POST':
        try:

            file = request.FILES['file']
            upload_to_hdfs(file, file.name)
                                       
            car_id = request.POST['car_id']
            client_id = request.POST['client_id']

            booking_date_str = str(request.POST['start_date'])
            return_date_str = str(request.POST['end_date'])

            # Convert the strings to datetime objects
            booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d")
            return_date = datetime.strptime(return_date_str, "%Y-%m-%d")

            car = Car.objects.get(car_id=car_id)
            clientObj = User.objects.get(id=client_id)

            #customer_email = {clientObj.email}
            #customer_name = {clientObj.first_name}

            if car.status != 'Available':
                return JsonResponse({'message': 'Car is already booked!'}, status=400)

            booking = Booking.objects.create(
                car_id=car,
                total_cost= ((return_date - booking_date).days) * car.cost_per_day,
                client_id=clientObj,
                status='Approved',
                booking_date=booking_date,
                return_date=return_date
            )

            car.status = 'Booked'
            car.save()

            # Publish event to Kafka
            #producer = Producer({'bootstrap.servers': settings.KAFKA_BROKER_URL})
            #producer.produce('bookingCreated', value=f"{booking.booking_id},{car_id},{customer_name},{customer_email}")
            #producer.flush()

            body = f"""Dear {clientObj.first_name} {clientObj.last_name},

        Thank you for booking with us! Here are your booking details:

        - **Booking Date:** {booking_date}
        - **Return Date:** {return_date}
        - **Total Amount to Pay:** {((return_date - booking_date).days) * car.cost_per_day} Rwf
        - **Driver Names :** {car.driver_id.first_name} {car.driver_id.last_name}
        - **Driver's phone Number :** {car.driver_id.phone}
        - **Driver's email :** {car.driver_id.email}
        We appreciate your trust in our service and look forward to serving you!

        Best regards,
        ACE-DS/DataMining/cohot6/Group No2
        """

            try:
                email_data = {
                    'recipient': clientObj.email,
                    'subject': 'Booking Confirmation Email',
                    'message': body,
                }
                send_email_to_kafka(json.dumps(email_data))
                return JsonResponse({'message': 'Email request sent to Kafka successfully!'})
            except Exception as e:
                return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
            
            
            #return JsonResponse({'message': 'Booking created successfully!'})

        except Car.DoesNotExist:
            return JsonResponse({'message': 'Car not found!'}, status=404)
        except Exception as e:
            return JsonResponse({'message': f'An error occurred: {str(e)}'}, status=500)

    cars = Car.objects.filter(status='Available')
    return render(request, 'create_booking.html', {'cars': cars})

    #form = BookingForm()   
    #cars_list = Car.objects.all()
    #return render(request,'clientPage.html',{'form':form,'cars_list':cars_list}) 

def bookingView(request):
    #cars = Car.objects.filter(status='Available')
    cars = Car.objects.all()
    return render(request, 'create_booking.html', {'cars': cars})



def email_form(request):
    return render(request, 'send_email.html')

def send_confirmation_email(request):
    """Handle the email submission."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email_data = {
                'recipient': 'munya.bernard@gmail.com',#data.get('munya.bernard@gmail.com'),
                'subject': 'Email Confirmation',
                'message': 'Please confirm your email address by clicking the link333.',
            }
            send_email_to_kafka(json.dumps(email_data))
            return JsonResponse({'message': 'Email request sent to Kafka successfully!'})
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
    return JsonResponse({'message': 'Invalid request method'}, status=405)



# Kafka Producer setup
producer = Producer({'bootstrap.servers': 'localhost:9092'})

def publish_to_kafka(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        message = json.dumps({'user_input': user_input})
        
        # Publish message to Kafka topic
        producer.produce('carBookedTopic', message)
        producer.flush()
        
        return JsonResponse({'status': 'success', 'message': 'Message sent to Kafka!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

   
def booking_view(request):
    bookingsList = Booking.objects.all()
    return render(request, 'bookings.html', {'bookingsList': bookingsList})



    
