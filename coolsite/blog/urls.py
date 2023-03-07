from django.contrib import admin
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:page>/', index, name='home'),
    path('about', about, name='about'),
    path('feedback', feedback, name='feedback'),
    path('one/<int:pid>/', one, name='one'),
    path('leet/', leet, name='leet'),
    path('translit/', translit, name='translit'),
#    re_path(r'^/?pYear/')
]