from django.urls import path
from .views import (
	storiesview,
	)

urlpatterns = [
    path('stories/',storiesview),
]
