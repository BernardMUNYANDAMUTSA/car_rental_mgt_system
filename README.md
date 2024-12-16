#### Module Title: Cloud Computing and Web Programming
#### Group II, Members:
  - MUNYANDAMUTSA Bernard: 220001209
  - MUHIRE Francis: 220019857
  - MUKESHIMANA Illumine: 223027716

# Project Title "Car Rental Management System"

## Context and Problem Statement
Car rental businesses operate in a highly dynamic environment where real-time data synchronization is essential for smooth operations. A car rental management system involves multiple interconnected processes, such as booking cars, managing fleet availability, and sending notifications to customers. Without effective communication between these processes, the system may face issues such as:

- Double-booking of cars due to delayed updates.
  
- Inconsistent data between booking and fleet management systems.

- Delayed notifications, reducing customer satisfaction.
  
To solve these issues, this project proposes an event-driven architecture that uses Apache Kafka to handle real-time communication between services.

## Proposed Solution

To address these challenges, the Car Rental Management System integrates Apache Kafka for real-time communication. Kafka ensures the system remains responsive and scalable, providing near-instant updates across services like fleet management, notification handling, and 

monitoring dashboards.

## Objectives
1. Online services
   
   - To offer a user-friendly web application that empowers our clients to book a car conveniently, anytime and anywhere.
     
   - Simplifying the car rental process for both administrators and customers
     
3. Real-Time Monitoring:
   
   - Maintaining a systematic record of available cars, drivers, and bookings
     
   - Provide a user-friendly dashboard for administrators to monitor bookings and car availability.
  
5. Enhanced Customer Experience:
   - Send immediate notifications for bookings and maintain accurate fleet availability to avoid inconvenience.
   - Providing a scalable and user-friendly interface for future enhancements
     
6. Decoupled Services:
   
  - Design modular and independent services (e.g., booking, fleet management, notifications) that communicate through Kafka.
    
6. Scalability:

   Use Kafka to handle increasing volumes of messages/events without performance degradation.
   
7. Integrate cloud services like AWS MySQL, Hadoop, and Kafka for advanced functionality

## System Overview
The Car Rental Management System is structured around three main entities:

**Car**: Contains details about each vehicle like car_id(pk) ,plate_number ,model ,year ,color ,transmission ,cost_per_day ,status(availability) ,driver_id(fk).

**Driver**: Contains details about the drivers, including their driver_id(pk), first_name, last_name, driving_license, email, phone.

**Booking**: Contains details about customer bookings, linking booking_id(pk), booking_date, return_date, total_cost, status, client_id(fk), car_id(fk).

In addition we django **Auth_user** table to hold details of system users(admin or clients), details include: id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined

These entities are interconnected to ensure seamless operations.

## Installation Instructions

### Prerequisites

  - Software/Tools: Python (3.x): For Django framework and related development
  - Pip: To manage Python packages
  - Django installed
  - Kafka installed, configured and running. Set up Zookeeper (required for Kafka operation)
  - Hadoop installed, configured and running. 
  - Text Editor/IDE: VS Code, PyCharm, or any other code editor.
  - Internet for AWS services, particularly RDS (Relational Database Service) to MySQL
  - MySQL Workbench (optional) for database management.
  - Browser: Chrome, Firefox, or any modern web browser for testing
  - 
## Installation Instructions (Project Setup)

- Clone the project from git via this link: https://github.com/BernardMUNYANDAMUTSA/car_rental_mgt_system.git
- Open the project in your IDE
- In your trminal/ cmd : cd car_rental_mgt_system
- Run Zookeeper: .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
- Run Kafka: .\bin\windows\kafka-server-start.bat .\config\server.properties
- Create Kafka topic called "emailConfirmationTopic": .\bin\windows\kafka-topics.bat --create --topic emailConfirmationTopic --bootstrap-server localhost:9092
- Run Hadoop services: start-all.cmd
- Get ready Kafka Consumer:
    - python manage.py shell
    - from rental_app.kafka_consumer import kafka_consumer
    - kafka_consumer()
  
![image](https://github.com/user-attachments/assets/f47a2044-97dd-40ad-8857-e9304c64ee88)


- Run server: python manage.py runserver

## Usage (User Documentation )
First of all, the system has two kind of users: System Administrator(Superuser) and Client

### Login Page
The Login Page serves as the secure gateway to the system, designed to accommodate both Admin and Client users. It features intuitive fields for entering a Username and Password, along with a prominent Login button to access the system. For new users, an accessible Registration Link is provided, enabling quick and easy account creation.

This page ensures robust security by handling both authentication (verifying user identity) and authorization (granting appropriate access based on user roles). Whether you're an administrator managing the system or a client utilizing its features, the login page guarantees a seamless and secure entry point.
![image](https://github.com/user-attachments/assets/e6efef0a-f1b3-4daa-aedf-43b5c232509a)

### Administrator Homepage
Let login as "Administrator" **(credentials for admin: username= 12345 , password= Bernard )**,
Admin Dashboard: The following image shows the admin dashboard of the Car Rental Management System. It provides an overview of key metrics, such as the number of subscribers, available cars, booked cars, approved bookings, bookings pending for approval and total income (in Rwandan Francs). The interface appears user-friendly with clear navigation options and quick access to system features like driver registration menu, car registration menu, and view bookings menu.
![image](https://github.com/user-attachments/assets/b81c8359-81bf-4db8-a6de-48cf8557c04f)

### Driver management form

The following interface is for CRUD (Create, Read, Update, Delete), it help system admin to record new driver,view all drivers, edit existing driver's information and do deletion of existing driver record.
![image](https://github.com/user-attachments/assets/60d0fdeb-2557-48c9-8f4d-b8bb0a2f42cd)

When you click on Edit button, the system gives you interface for editing existing information then click update button
![image](https://github.com/user-attachments/assets/49f5c532-d49c-4cbc-9721-9237faed28aa)

When you click on Delete button, the system prompt comfirmation message before deletion as follow:
![image](https://github.com/user-attachments/assets/93297bf3-68e7-40f5-ba34-6465238ada47)

### New car registration form
The following interface help admistrator to record a new car and immediately assigned to a driver (in drivers selection box) then click Submit button.
![image](https://github.com/user-attachments/assets/31d9a8a6-464d-4bad-83bb-6f07ea25bb7e)

### Bookings management interface

The following interface help admistrator, to view all bookings transactions with status. This interface also help admin to approve by click on Approve button or reject a booking by click on Cancel for the pending bookings.

![image](https://github.com/user-attachments/assets/8114675f-c675-435c-94c4-a078c34fe54c)


## Login as Client

 To login the system, new user have to sign-up and get username and password. The following Sign-Up page allows users to create an account by providing personal information, enabling access to services or features.
 ![image](https://github.com/user-attachments/assets/55b72941-f8e3-4883-b559-e5b5f4597787)

 ## Client Home
Once a user entered valid usernam and password on login page. The system displays availables cars ready for booking, pending cars waiting for approvals and booked cars
![image](https://github.com/user-attachments/assets/e6f6ef2e-d8df-4909-9f61-e75f2b59f6a8)
**(credentials for client Muhire Francis: username= 12347 , password= Bernard )**

**NOTE:** System can not allow user to book a car which is already booked or pening for approval, system allow booking for availables cars by click on **Book Now** button. 

When a client, click on Book Now button, the system open a window to provide booking start date, return date and input field to upload payment receipt as follow:
![image](https://github.com/user-attachments/assets/b9fc9929-a744-41b8-97ff-85ad3bff803d)

After booking submssion, the system change the car booking status to **Pending** and can not be booked by any other client. 
![image](https://github.com/user-attachments/assets/1fd40de4-1497-4a84-bf47-380f820b8ffd)

Also after submission, using kafka cunsumer, the syetm send submission confirmation email to the client's email

![image](https://github.com/user-attachments/assets/3adc360b-0eaf-4dd4-aebf-a813991d45f4)

![image](https://github.com/user-attachments/assets/ecb75bba-fe79-4590-855c-2adb01cdff01)

Also, the system upload the submited payment receipt to HDFS in uploads directory as follow:
![image](https://github.com/user-attachments/assets/f3c60252-6803-4899-8edd-95e4d785097b)

![image](https://github.com/user-attachments/assets/5630179e-aaba-4e3e-acbc-e0d2c5d26406)

We have seen that the booking submitted successfuly and waiting approval. The system admin login, verify payment receipt and approve booking request as follow:

![image](https://github.com/user-attachments/assets/d4647a48-3bbb-42cf-8c9a-84305a750d8b)

By founding that there are some booking pending for approval, then the admin click on Bookings menu for approval or cancel
![image](https://github.com/user-attachments/assets/fcd67d77-bac3-4c1a-8ac3-005a1932d11f)

When the booking is approved, automatically the system increased number of approved bookings, booked cars, total income (Rwf) and decrease available cars, number of pending bookings.
![image](https://github.com/user-attachments/assets/7fd8470e-37d6-4f42-a44a-62866cacedd8)

Also after approval, using kafka cunsumer, the system send approval confirmation email to the client composed by Driver'details and contacts
![image](https://github.com/user-attachments/assets/bcf95145-385e-47e5-b25d-4c0ed0a561e2)

Back to the client portal, the system shows that the car changed the status to **booked**(Not available for booking) as follow:

![image](https://github.com/user-attachments/assets/44e6bb17-e54d-4898-8d67-b207982db836)

## Technologies Used

- Framework: Django
- Frontend: We used Bootstrap, Javascript, HTML, CSS, and AJAX for designing responsive and interactive user interfaces.

  For instance,  AJAX was used in the project on driver deletion:
  ![image](https://github.com/user-attachments/assets/23fc406e-a84c-4978-bb71-e3decf46b152)

- Tools:
    - Kafka for Real-Time Communication
    - Hadoop (hdfs) for for managing uploaded payment receipts
- MySQL Database on AWS : We connected our Django application to the AWS-hosted MySQL database.
  
## Members' contribution

### - MUNYANDAMUTSA Bernard: 220001209 :
Mr.Bernard 's contributions are the followings:
- Setting-up django, created project and application.
- - Frontend design usign Bootstrap, Javascript and AJAX for designing responsive and interactive user interfaces.
- Installation of kafka , created Kafka topic, created kafka producer and kafka consumer into our project  
- Installation of hadoop, integrate it into our project and upload attached payment receipt files into HDFS
- Development of admin dashboard(Fronted and backend) to show in summary total number of subscribers (registerd Clients), total number of available cars ready for booking, total number of cars already booked, total number of bookings approved, total number of bookings waiting for approval(Pendings) and total Income amount in Rwf 

### - MUHIRE Francis: 220019857

Mr.Francis 's contributions are the followings:
- Development of user management module, includes client sign-up and login with authentication and authorization
- Used Amazon RDS to create and configure a MySQL database called "carrentaldb2".
- Connected our Django application(Car Rental Management System) to the AWS-hosted MySQL database

### - MUKESHIMANA Illumine: 223027716

Mrs. Illumine 's contributions are the followings:
- Frontend design usign HTML and CSS for designing responsive and interactive user interfaces
- Database design and creation of models
- Development of CRUD (Create, Read, Update an Delete) on drivers table
- System documentation (The case study, objectives, user guide, Technologies Used, etc..)

















































