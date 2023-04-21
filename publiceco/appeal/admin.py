from django.contrib import admin

from appeal.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'news_text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(news, NewsAdmin)

class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'appeal_text')

admin.site.register(appeal, AppealAdmin)

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'articles_text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(articles, ArticlesAdmin)

# class SensorDataAdmin(admin.ModelAdmin):
#     list_display = ('id', )
#     list_display_links = ('id', )
#     search_fields = ('id', )
#
# admin.site.register(SensorData, SensorDataAdmin)

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp')
    list_display_links = ('id', 'timestamp')
    search_fields = ('id', 'timestamp')

admin.site.register(SensorData2, SensorDataAdmin)