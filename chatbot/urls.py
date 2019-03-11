from django.urls import path
from .views import (
	chatbotview,
	)

urlpatterns = [
    path('chatbot/',chatbotview),
]
