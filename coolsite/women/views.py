from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from time import strftime

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request,cat_id=0):
    if(cat_id == 0):
        posts = Women.objects.all();
    else:
        posts = Women.objects.filter(cat=cat_id);

    if len(posts) == 0:
        raise Http404();

    cats = Category.objects.all();
    params = {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cat_selected': cat_id, 'cats': cats};
    return render(request, 'women/index.html', params)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Добавить станицу'})

def contact(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Контакты'})

def show_post(request, post_id):
    women = Women.objects.get(pk=post_id);
    cats = Category.objects.all();
    params = {'w':women, 'menu': menu, 'title': women.title, 'strftime':strftime, 'cats':cats, 'cat_selected': women.cat.pk}

    # print(women.birthday.time.strftime('%Y:%m:%d'))

    return render(request, 'women/post.html', context=params)

def login(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Войти'})

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
