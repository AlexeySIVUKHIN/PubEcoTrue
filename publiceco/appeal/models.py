from django.db import models
from django.urls import reverse
class appeal(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    city = models.CharField(max_length=255, verbose_name='Ваш населённый пункт')
    appeal_text = models.TextField(blank=True, verbose_name='Текст обращения')
    e_mail = models.EmailField(max_length=254, verbose_name='Электронный адрес для связи', blank=True, null=True)
    phone_number = models.IntegerField(verbose_name='Телефонный номер для связи', blank=True, null=True)
    photo = models.ImageField(upload_to="photos/appeals/%Y/%m/%d/", verbose_name='Фотография нарушения, если требуется', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('appeals', kwargs={'appeals_id': self.pk})
    class Meta:
        verbose_name = 'Обращения'
        verbose_name_plural = 'Обращения'
        ordering = ['time_create', 'name']

class news(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    text = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/news/%Y/%m/%d/", verbose_name='Фотография', blank=True)
    photo_2nd = models.ImageField(upload_to="photos/news/%Y/%m/%d/", verbose_name='Фотография2', blank=True)
    photo_3rd = models.ImageField(upload_to="photos/news/%Y/%m/%d/", verbose_name='Фотография3', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create', 'title']

class articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    text = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/articles/%Y/%m/%d/", verbose_name='Фотография', blank=True)
    photo_2nd = models.ImageField(upload_to="photos/articles/%Y/%m/%d/", verbose_name='Фотография2', blank=True)
    photo_3rd = models.ImageField(upload_to="photos/articles/%Y/%m/%d/", verbose_name='Фотография3', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_create', 'title']
