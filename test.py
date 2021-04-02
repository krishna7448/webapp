import json, requests, redis, websockets, random, time
from websocket import create_connection
uri = 'ws://localhost:8080/ws/polData/'
websockets.connect(uri)

#ws = create_connection("ws://localhost:8080/ws/polData/")
#ws.send("Hello, World")


#ws.connect('ws://localhost:8000/ws/polData/')

