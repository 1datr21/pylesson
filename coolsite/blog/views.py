from django.shortcuts import render, HttpResponse;
from blog.models import Blog;
from django.core.paginator import Paginator

menu = {'home':"Главная", 'about': "О нас", 'feedback': "Обратная связь"}

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

def one(request, pid):
    post = Blog.objects.get(pk=pid)
    return render(request, 'blog/one.html', {'menu': menu, 'title': post.title, 'post':post});
    #return HttpResponse(f"<h1>One article #{pid}</h1>");

