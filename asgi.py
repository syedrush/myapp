import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatbot.routing
import quizzes.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartedu.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatbot.routing.websocket_urlpatterns +
            quizzes.routing.websocket_urlpatterns
        )
    ),
})
