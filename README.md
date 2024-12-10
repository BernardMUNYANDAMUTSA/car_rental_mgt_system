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

**Car**: Contains details about each vehicle like car_id(pk),plate_number, model,year,color,transmission,cost_per_day,status(availability),driver_id.

**Driver**: Contains details about the drivers, including their availability and assignments.

**Booking**: Contains details about customer bookings, linking cars, drivers, and rental periods.

**These** entities are interconnected to ensure seamless operations.


