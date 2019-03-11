from django.urls import path
from .views import (
	helplineview,
	)

urlpatterns = [
    path('helpline/',helplineview),
]
