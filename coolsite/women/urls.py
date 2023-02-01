from django.contrib import admin
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:cat_id>/', index, name='category'),
 #   path('category/<int:cid>/', categories),
    path('addpage', addpage, name='add_page'),
#    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),

]

