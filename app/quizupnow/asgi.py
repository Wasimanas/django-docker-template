import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import quiz.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizupnow.settings') 


django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(quiz.routing.websocket_urlpatterns)
    ),
})

