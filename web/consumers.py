from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep

class WSConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope)
        self.accept()
        for i in range(10):
            self.send(json.dumps({'message':randint(1,100)}))
            sleep(1)