import os
import sys
import django

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_rental_mgt_system.settings")
django.setup()

from rental_app.models import Car
from confluent_kafka import Consumer, KafkaException, KafkaError
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def consume_user_input_messages():
    consumer = None
    try:
        # Initialize Kafka consumer
        consumer = Consumer({
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'user_input_group ',
            'auto.offset.reset': 'earliest'
        })
        consumer.subscribe(['carBookedTopic'])

        channel_layer = get_channel_layer()

        while True:
            try:
                # Poll for Kafka messages
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print("End of partition reached.")
                        continue
                    else:
                        raise KafkaException(msg.error())

                event = msg.value().decode('utf-8')
                print(f"Received user input: {event}")

                # Push update to WebSocket group
                try:
                    async_to_sync(channel_layer.group_send)(
                        'user_input_updates',
                        {
                            'type': 'send_booking_update',
                            'message': event,
                        }
                    )
                except Exception as ws_error:
                    print(f"WebSocket error: {ws_error}")

            except KafkaException as ke:
                print(f"Kafka error while polling: {ke}")
            except Exception as general_error:
                print(f"General error while processing message: {general_error}")

    except Exception as initialization_error:
        print(f"Error during Kafka consumer initialization: {initialization_error}")

    finally:
        # Clean up Kafka consumer
        if consumer is not None:
            try:
                consumer.close()
                print("Kafka consumer closed.")
            except Exception as close_error:
                print(f"Error while closing Kafka consumer: {close_error}")

if __name__ == '__main__':
    consume_user_input_messages()