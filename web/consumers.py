from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from time import sleep
import asyncio
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
#server status
import psutil, os


class WSConsumer(AsyncWebsocketConsumer):
    name = 'DashConsumer'
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']

        #print(self.scope)
        #print('connected! ', event)
        await self.accept()


    async def receive(self, text_data):
        dash = json.loads(text_data).get('dash')
        cpu = psutil.cpu_percent()
        vram = psutil.virtual_memory()
        print(cpu)
        ram_percent = vram[2]
        print(ram_percent)
        #print(dash)
        data={
            'cpu':cpu,
            'ram':ram_percent,
            'message':randint(1,100)
        }
        await self.send(text_data=json.dumps(data))

    async def live_data(self, event):
        # Here helper function fetches live score from DB.
        for i in range(10):
            await self.send(text_data=json.dumps({'message':randint(1,100)}))
            sleep(1)

    async def disconnect(self, message):
        # Leave room group
        await self.channel_layer.group_discard(
            self.channel_name
        )