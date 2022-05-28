from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name,
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected gest'}))

    def receive(self, text_data):
        print(text_data)
        self.send(text_data=text_data)
        pass

    def disconnect(self, *args, **kwargs):
        print('disconnected')

    
    def send_notification(self, event):
        print('send_notifications', event)
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))
        print('send_notifications2')


class TestConsumer2(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = 'test_consumer2'
        self.room_group_name = 'test_consumer2_group'

        await (self.channel_layer.group_add)(
            self.room_group_name, self.channel_name,
        )
        await self.accept()
        await self.send(text_data=json.dumps({'status': 'connected Consumer 2'}))

    async def receive(self, text_data):
        # await print(text_data)
        await self.send(text_data=text_data)

    async def disconnect(self, *args, **kwargs):
        print('disconnected')

    
    async def send_notification(self, event):
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload': data}))
