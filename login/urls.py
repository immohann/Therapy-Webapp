from django.urls import path
from django.urls import re_path
from .views import (
	loginregisterview,
	)

urlpatterns = [
    path('login/',loginregisterview),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate'),
]
