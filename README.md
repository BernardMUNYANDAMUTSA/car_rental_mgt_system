# Car Rental Management System

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
- Run server: python manage.py runserver

## Usage (User Documentation )






