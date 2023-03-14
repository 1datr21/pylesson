from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from time import strftime

from .models import *



def index(request, cat_slug=None):

    if(cat_slug==None):
        posts = Women.objects.all();
    else:
        categ = Category.objects.filter(slug=cat_slug)
        posts = Women.objects.filter(cat= categ[0].pk);
    print(posts)
    if len(posts) == 0:
        raise Http404();

    params = {'posts': posts, 'title': 'Главная страница', 'cat_slug_selected': cat_slug};
    return render(request, 'women/index.html', params)

def about(request):
    return render(request, 'women/about.html', { 'title': 'О сайте'})

def addpage(request):
    return render(request, 'women/about.html', { 'title': 'Добавить станицу'})

def contact(request):
    return render(request, 'women/about.html', { 'title': 'Контакты'})

def show_post(request, post_slug):

    women = get_object_or_404(Women, slug=post_slug)

    params = {'w':women, 'title': women.title, 'strftime':strftime, 'cat_selected': women.cat.pk}

    # print(women.birthday.time.strftime('%Y:%m:%d'))

    return render(request, 'women/post.html', context=params)

def login(request):
    return render(request, 'women/about.html', { 'title': 'Войти'})

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
