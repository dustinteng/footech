#channels version of django views, can initiate request to clients too!!

import json
from channels.generic.websocket import WebsocketConsumer

class GuiConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'you are connected'
        }))