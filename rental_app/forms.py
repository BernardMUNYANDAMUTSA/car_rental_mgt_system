from django import forms  
from rental_app.models import Car,Driver,Booking

class CarForm(forms.ModelForm):  
    class Meta:  
        model = Car  
        fields = "__all__"

class DriverForm(forms.ModelForm):  
    class Meta:  
        model = Driver  
        fields = "__all__"

class BookingForm(forms.ModelForm):  
    class Meta:  
        model = Booking  
        fields = "__all__"
        file = forms.FileField()