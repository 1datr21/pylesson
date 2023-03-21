from django.contrib import admin
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('', WomenHome.as_view(), name='home'),
    #path('category/<slug:cat_slug>/', index, name='category'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('addpage', AddPage.as_view(), name='add_page'),
#    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),

]

