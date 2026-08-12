import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.channel_layer.group_add(
                "chat",
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "chat",
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        user = self.scope["user"]
        

        message = await sync_to_async(Message.objects.create)(
            user=user,
            content=data["message"]
        )
        
        local_time = timezone.localtime(message.timestamp)
        timestamp = local_time.strftime("%H:%M")
        
        avatar = user.image.url if user.image and hasattr(user.image, 'url') else 'https://bumper-stickers.ru/26762-thickbox_default/znak-voprosa.jpg'
        
        await self.channel_layer.group_send(
            "chat",
            {
                "type": "chat.message", 
                "id": data.get("id", str(message.id)), 
                "message": data["message"],
                "username": data["username"],
                "avatar": avatar,
                "timestamp": timestamp,
                "is_current": False
            }
        )

    async def chat_message(self, event):
        if self.scope["user"].username == event["username"]:
            event["is_current"] = True
        
        await self.send(text_data=json.dumps(event))