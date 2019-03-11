from django.urls import path
from .views import (
	dietitianview,
	)

urlpatterns = [
    path('dietitian/',dietitianview),
]
