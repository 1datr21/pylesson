from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Содержимое")
    birthday = models.DateField(null=True, blank=True, verbose_name="День рождения")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name="Категория")
    foreign_agency = models.BooleanField(default=False, verbose_name="Признана иностранным агентом")

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['id']

    def __str__(self):
        return self.title;

    def get_absolute_url(self):
        return reverse('women:post', kwargs={'post_slug':self.slug});

    def get_item_url(self):
        return reverse('women:post', kwargs={'post_id':self.pk});

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name;

    def get_absolute_url(self):
        return reverse('women:category', kwargs={'cat_slug':self.slug});