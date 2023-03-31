from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.cache import  cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60)(WomenHome.as_view()), name='home'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('addpage', AddPage.as_view(), name='add_page'),
    path('about', about, name='about'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),

]



