from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from time import strftime
from women.forms import *
from django.views.generic import ListView, DetailView, CreateView
from .models import *

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    #extra_context = {'title':'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Главная страница'
        context['cat_slug_selected']= 0;
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False
    #extra_context = {'title':'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categ = Category.objects.filter(slug=self.kwargs['cat_slug'])
        context['title']='Категория:'+categ[0].name
        context['cat_slug_selected']= self.kwargs['cat_slug'];
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True, cat__slug=self.kwargs['cat_slug'])

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    context_object_name = 'w'
    allow_empty = False
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['w']
        context['cat_slug_selected'] = context['w'].cat.slug
        context['strftime']=strftime
        #context['cat_selected']= context['w'].cat.slug
        return context

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)

        context['title'] = 'Добавление статьи'
        context['cat_slug_selected'] = 0

        return context

def about(request):
    return render(request, 'women/about.html', { 'title': 'О сайте'})
"""
def addpage(request):
    if request.method=='POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', { 'title': 'Добавить станицу','form':form})
"""

def contact(request):
    return render(request, 'women/about.html', { 'title': 'Контакты'})
"""
def show_post(request, post_slug):

    women = get_object_or_404(Women, slug=post_slug)

    params = {'w':women, 'title': women.title, 'strftime':strftime, 'cat_selected': women.cat.pk}

    # print(women.birthday.time.strftime('%Y:%m:%d'))

    return render(request, 'women/post.html', context=params)"""

def login(request):
    return render(request, 'women/about.html', { 'title': 'Войти'})

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
