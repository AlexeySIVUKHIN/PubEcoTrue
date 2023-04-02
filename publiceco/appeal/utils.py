from .models import *

menu = [
        {'title': "Новости", 'url_name': 'news'},
        {'title': "Статьи", 'url_name': 'articles'},
        {'title': "Оставить обращение", 'url_name': 'add_appeal'},
        {'title': "О Корпусе", 'url_name': 'about'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context