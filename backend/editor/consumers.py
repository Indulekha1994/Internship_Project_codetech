import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Document

class EditorConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.doc_id = self.scope["url_route"]["kwargs"]["doc_id"]
        self.room_group_name = f"document_{self.doc_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data["content"]

        await self.save_document(content)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_update",
                "content": content
            }
        )

    async def send_update(self, event):
        await self.send(text_data=json.dumps({
            "content": event["content"]
        }))

    @database_sync_to_async
    def save_document(self, content):
        doc, created = Document.objects.get_or_create(
            id=self.doc_id,
            defaults={"title": "Untitled"}
        )

        doc.content = content
        doc.save()