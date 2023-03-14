from django.shortcuts import render, HttpResponse;

import blog.forms
from blog.models import Blog;
from django.core.paginator import Paginator
from blog.forms import *;
from django.core import serializers
from django.http import JsonResponse

menu = {'home':"Главная", 'about': "О нас", 'feedback': "Обратная связь", 'translit':"Транслит по-контр-страйковски"}

# Create your views here.
def index(request, page=1):
    page_size = 6;
    paginator = Paginator(Blog.objects.all(), page_size);
    page_number = 1;
    page_obj = paginator.get_page(page);
    chuncked = list();
    ch_size = 2;
    # чанкаем посты по 2
    for i in range(0,len(page_obj), ch_size):
        chuncked.append(page_obj[i:i+ch_size]);
    print(chuncked)
    return render(request, 'blog/index.html', {'menu':menu, 'title':'Главная', 'posts':chuncked, 'page_obj':page_obj});

def about(request):
    return render(request, 'blog/about.html', {'menu':menu, 'title':'О нас'});

def feedback(request):
    return render(request, 'blog/feedback.html', {'menu': menu, 'title': 'Обратная связь'})

def translit(request):
    if request.method == 'POST':
        theform = blog.forms.LeetForm(request.POST)
        if theform.is_valid():
            symbols = {'А': 'A', 'Б': '6', 'В': 'B', 'Г': 'r', 'Д': 'D',
                 'Е': 'E','Ё': 'E', 'Ж':'3X', 'З':'3', 'И': 'u','Й': 'u', 'К': 'K', 'Л': 'Jl', 'М': 'M','Н':'H','О':'O','П':'n','Р':'P','С':'C',
                       'Т':'T','У':'у','Ф':'qp','Х':'X','Ч':'4','Щ':'LLI','Щ':'LLIb','Ц':'Ll','Ь':'b','Ъ':'1b','Ы':'bl','Э':'-)','Ю':'I0','Я':'9l'}
            str = theform.cleaned_data.get("content")
            result = str.upper().translate(str.maketrans(symbols))
            res_data = {'result': result, 'result_lcase':result.lower() }
            return JsonResponse(res_data)
    else:
        theform = blog.forms.LeetForm()

    return render(request, 'blog/translit.html', {'menu': menu, 'title': 'Транслит', 'form': theform});

# translate the text
def leet(request):
    data = [2.1, 8]
    return HttpResponse(data, content_type='application/json')
def one(request, pid):
    post = Blog.objects.get(pk=pid)
    return render(request, 'blog/one.html', {'menu': menu, 'title': post.title, 'post':post});
    #return HttpResponse(f"<h1>One article #{pid}</h1>");

