from confluent_kafka import Consumer
from django.core.mail import send_mail
from django.conf import settings

def consume_notifications():
    print("=============================>")
    consumer = Consumer({
        'bootstrap.servers': settings.KAFKA_BROKER_URL,
        'group.id': 'notification_group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['bookingCreated'])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        event = msg.value().decode('utf-8').split(',')
        booking_id, car_id, customer_name, customer_email = event

        send_mail(
            f"Booking Confirmation - ID: {booking_id}",
            f"Dear {customer_name},\n\nYour booking for car ID {car_id} is confirmed.",
            settings.EMAIL_HOST_USER,
            [customer_email],
        )
        print(f"Email sent to {customer_email}.")
