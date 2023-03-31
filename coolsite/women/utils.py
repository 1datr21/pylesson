from django.db.models import Count

from women.forms import *
from django.core.cache import cache

menu = [{'title':"О сайте",'url':'women:home'},
        {'title':"Добавить статью",'url':'women:add_page'},
        {'title':"Обратная связь",'url':'women:contact'}]

class DataMixin:
    def get_basic_data(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('women'))
            cache.set('cats',cats, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
           del user_menu[1]

        context['menu']=user_menu
        context['cats']=cats
        if 'cat_selected' not in context:
            context['cat_selected']=0
        return context

class DataListMixin(DataMixin):
    model = Women
    paginate_by = 4
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = True