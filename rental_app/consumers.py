import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BookingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'booking_updates'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_booking_update(self, event):
        # Send the update to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))



class UserInputConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'user_input_updates'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_booking_update(self, event):
        # Send the update to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
