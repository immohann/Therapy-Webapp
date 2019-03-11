from django.urls import path
from .views import (
	therapistview,
	)

urlpatterns = [
    path('therapist/',therapistview),
]
