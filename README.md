# Car Rental Management System

## Context and Problem Statement
Car rental businesses operate in a highly dynamic environment where real-time data synchronization is essential for smooth operations. A car rental management system involves multiple interconnected processes, such as booking cars, managing fleet availability, and sending notifications to customers. Without effective communication between these processes, the system may face issues such as:

- Double-booking of cars due to delayed updates.
- Inconsistent data between booking and fleet management systems.
- Delayed notifications, reducing customer satisfaction.
  
To solve these issues, this project proposes an event-driven architecture that uses Apache Kafka to handle real-time communication between services.

## Objectives
1. Online services
   - To offer a user-friendly web application that empowers our clients to book a car conveniently, anytime and anywhere.
   - Simplifying the car rental process for both administrators and customers
     
2. Real-Time Monitoring:
   - Maintaining a systematic record of available cars, drivers, and bookings
   - Provide a user-friendly dashboard for administrators to monitor bookings and car availability.
  
4. Enhanced Customer Experience:
   - Send immediate notifications for bookings and maintain accurate fleet availability to avoid inconvenience.
   - Providing a scalable and user-friendly interface for future enhancements
     
5. Decoupled Services:
  - Design modular and independent services (e.g., booking, fleet management, notifications) that communicate through Kafka.

## System Overview
The Car Rental Management System is structured around three main entities:

**Car**: Contains details about each vehicle like car_id(pk) ,plate_number ,model ,year ,color ,transmission ,cost_per_day ,status(availability) ,driver_id(fk).

**Driver**: Contains details about the drivers, including their driver_id(pk), first_name, last_name, driving_license, email, phone.

**Booking**: Contains details about customer bookings, linking booking_id(pk), booking_date, return_date, total_cost, status, client_id(fk), car_id(fk).

In addition we django **Auth_user** table to hold details of system users(admin or clients), details include: id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined

These entities are interconnected to ensure seamless operations.


