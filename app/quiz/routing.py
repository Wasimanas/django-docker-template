from django.urls import path 
from quiz import consumers 


websocket_urlpatterns = [
        path('ws/quiz/<slug:quizCategorySlug>/',consumers.QuizConsumer.as_asgi(),name='quiz'),
        ]

