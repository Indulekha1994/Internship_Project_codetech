import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chatroom.models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        # Send to group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'send_message',   # triggers send_message
                'message': data
            }
        )

    async def send_message(self, event):
        data = event['message']

        # Save message to DB
        await self.create_message(data)

        # Send to WebSocket
        await self.send(text_data=json.dumps({
            'message': {
                'sender': data['sender'],
                'message': data['message']
            }
        }))

    @database_sync_to_async
    def create_message(self, data):
        room_name = self.scope['url_route']['kwargs']['room_name']
        get_room = Room.objects.get(room_name=room_name)
        new_message = Message(room=get_room, sender=data['sender'], message=data['message'])
        new_message.save()
