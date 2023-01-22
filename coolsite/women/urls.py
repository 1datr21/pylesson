from django.contrib import admin
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:cid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]

