from django import template
from women.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html')
def categories_list(sort_params=None, cat_slug_selected=0):
    if not sort_params:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort_params)
    return { 'cats':  cats, 'cat_slug_selected': cat_slug_selected }

@register.inclusion_tag('women/menu.html')
def header_menu(selected_item=None):

    menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
    return { 'menu':  menu, 'selected_item':selected_item }