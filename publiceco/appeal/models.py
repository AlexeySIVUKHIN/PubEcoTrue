from django.db import models
from django.urls import reverse
from django.utils import timezone
import pytz
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
        return reverse('articles', kwargs={'articles_slug': self.slug})

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_create', 'title']


# class SensorDataTable(ExportModelOperationsMixin('SensorDataTable'), models.Model):
#     pm1 = models.CharField(max_length=255, verbose_name='pm1')
#     pm2 = models.CharField(max_length=255, verbose_name='pm2')
#     temperature = models.CharField(max_length=255, verbose_name='temperature')
#     humidity = models.CharField(max_length=255, verbose_name='humidity')
#     pressure = models.CharField(max_length=255, verbose_name='pressure')
#     day = models.DateField(auto_now_add=True, verbose_name='День')
#     timeOfDay = models.DateTimeField(auto_now=True, verbose_name='Время')
#
#     def get_absolute_url(self):
#         return reverse('SensorDataTable', kwargs={'SensorDataTable_id': self.pk})
#
#     class Meta:
#         verbose_name = 'Замеры'
#         verbose_name_plural = 'Замеры'
#         ordering = ['-timeOfDay', 'timeOfDay']


# class SensorDataTable(models.Model):
#     # esp8266id = models.CharField(max_length=255,blank=True,verbose_name='esp8266id', default=None, null=True)
#     # software_version = models.CharField(max_length=255,blank=True,verbose_name='software_version', default=None, null=True)
#     # sensordatavalues = models.CharField(max_length=255,blank=True,verbose_name='sensordatavalues', default=None, null=True)
#     SDS_P1 = models.CharField(max_length=255,blank=True,verbose_name='pm10', default=None, null=True)
#     SDS_P2 = models.CharField(max_length=255,blank=True,verbose_name='pm2.5', default=None, null=True)
#     BME280_temperature = models.CharField(max_length=255,verbose_name='BME280_temperature', default=None, null=True)
#     BME280_pressure = models.CharField(max_length=255,verbose_name='BME280_pressure',default=None, null=True)
#     BME280_humidity = models.CharField(max_length=255,verbose_name='BME280_humidity', default=None, null=True)
#     samples = models.CharField(max_length=255,verbose_name='samples', default=None, null=True)
#     min_micro = models.CharField(max_length=255,verbose_name='min_micro', default=None, null=True)
#     max_micro = models.CharField(max_length=255,verbose_name='max_micro', default=None, null=True)
#     signal = models.CharField(max_length=255,verbose_name='signal', default=None, null=True)
#     interval = models.CharField(max_length=255,verbose_name='interval', default=None, null=True)
#     timestamp = models.DateTimeField(auto_now=True, verbose_name='Время', null=True)
#
#     def get_absolute_url(self):
#         return reverse('SensorDataTable', kwargs={'SensorDataTable_id': self.pk})
#
#     class Meta:
#         verbose_name = 'Замеры'
#         verbose_name_plural = 'Замеры'
#         ordering = ['-timestamp', 'timestamp']


class SensorData2(models.Model):
    esp8266id = models.PositiveIntegerField()
    SDS_P1 = models.DecimalField(max_digits=8, decimal_places=2)
    SDS_P2 = models.DecimalField(max_digits=8, decimal_places=2)
    BME280_temperature = models.DecimalField(max_digits=8, decimal_places=2)
    BME280_pressure = models.DecimalField(max_digits=8, decimal_places=2)
    BME280_humidity = models.DecimalField(max_digits=8, decimal_places=2)
    samples = models.PositiveIntegerField()
    min_micro = models.PositiveIntegerField()
    max_micro = models.PositiveIntegerField()
    interval = models.PositiveIntegerField()
    signal = models.IntegerField()
    timestamp = models.DateTimeField(verbose_name='Время', default=timezone.now)

    def save(self, *args, **kwargs):
        timezone.activate(pytz.timezone("Europe/Moscow"))
        super().save(*args, **kwargs)