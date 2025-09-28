from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatbotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')
        # For demo, echo the message with a hint
        response = f"AI Hint: You asked '{message}'. Here's a helpful tip!"
        await self.send(text_data=json.dumps({'response': response}))
