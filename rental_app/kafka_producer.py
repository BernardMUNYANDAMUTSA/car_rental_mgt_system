from confluent_kafka import Producer
from django.conf import settings

def kafka_producer():
    return Producer({'bootstrap.servers': settings.KAFKA_BROKER_URL})

def send_email_to_kafka(email_data):
    producer = kafka_producer()
    producer.produce(settings.KAFKA_EMAIL_TOPIC, value=email_data.encode('utf-8'))
    producer.flush()
