from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from time import strftime

from django.urls import reverse_lazy

from women.forms import *
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin

class WomenHome(DataListMixin, ListView):
    model = Women
    paginate_by = 4
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_basic_data(title='Главная страница')
        return {**context, **c_def}

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')


class WomenCategory(DataListMixin, ListView):
    model = Women
    paginate_by = 4
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = True
    #extra_context = {'title':'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categ = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_basic_data(title='Категория: '+categ.name, cat_slug_selected=categ.slug)
        #context['cat_slug_selected']= self.kwargs['cat_slug'];
        return {**context, **c_def}

    def get_queryset(self):
        return Women.objects.filter(is_published=True, cat__slug=self.kwargs['cat_slug']).select_related('cat')

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    context_object_name = 'w'
    allow_empty = False
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
    #    context['title'] = context['w']
        context['cat_slug_selected'] = context['w'].cat.slug
        context['strftime']=strftime
        c_def = self.get_basic_data(title=context['w'])
        return {**context, **c_def}
  #      return context

class AddPage(LoginRequiredMixin, DataMixin,CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    # LoginRequiredMixin
    success_url = reverse_lazy('women:home')
    login_url = reverse_lazy('women:home')
    # redirect_field_name = 'redirect_to'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_basic_data(title='Добавление статьи')
        return {**context, **c_def}

# @login_required
def about(request):
    paginator = Paginator(Women.objects.all(),3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'women/about.html', { 'menu':menu, 'page_obj':page_obj, 'title': 'О сайте'})

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('women:login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_basic_data(title='Регистрация')
        return {**context, **c_def}

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_basic_data(title='Авторизация')
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('women:home')

def logout_user(request):
    logout(request)
    return redirect('women:login')

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('women:home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_basic_data(title='Обратная связь')
        return {**context, **c_def}

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('women:home')


def login(request):
    return render(request, 'women/about.html', { 'title': 'Войти'})

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
