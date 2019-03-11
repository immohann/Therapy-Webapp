from django.urls import path
from .views import (
	survey_testview,
	)

urlpatterns = [
    path('test/',survey_testview),
]
