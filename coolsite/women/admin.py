from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','get_html_photo','birthday','is_published','foreign_agency')
    list_display_links = ('id', 'title')
    search_fields = ['title', 'content']
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title','slug','photo','get_html_photo','birthday','is_published','foreign_agency')
    readonly_fields = ('time_create','time_update','get_html_photo')
    save_on_top = False
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50" />')

    get_html_photo.short_description = "Превью фото"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Админко сайтега"
admin.site.site_header = "Админко сайтега"