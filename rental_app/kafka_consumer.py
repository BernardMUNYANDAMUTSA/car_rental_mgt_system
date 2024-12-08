import json
from confluent_kafka import Consumer
from django.core.mail import send_mail
from django.conf import settings

def kafka_consumer():
    consumer = Consumer({
        'bootstrap.servers': settings.KAFKA_BROKER_URL,
        'group.id': 'email-group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([settings.KAFKA_EMAIL_TOPIC])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            message_value = msg.value()
            if not message_value:
                print("Received empty message, skipping...")
                continue

            try:
                email_data = json.loads(message_value.decode('utf-8'))
                send_mail(
                    email_data['subject'],
                    email_data['message'],
                    settings.EMAIL_HOST_USER,
                    [email_data['recipient']],
                    fail_silently=False,
                )
                print(f"Email sent to {email_data['recipient']}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                print(f"Received message: {message_value}")
                continue

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()