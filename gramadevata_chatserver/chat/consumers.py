# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom
from .serializers import MessageSerializer1            

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.village_id = self.scope['url_route']['kwargs'].get('village_id')
        self.user_id = self.scope['url_route']['kwargs'].get('user_id')
        self.room_group_name = f'chat_{self.village_id}_{self.user_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
 
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')
        
        # Save message to the database
        await self.save_message(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    
    @database_sync_to_async
    def save_message(self, message):
        ChatRoom.objects.create(
            user_id=self.user_id,
            village_id=self.village_id,
            message=message
        )
