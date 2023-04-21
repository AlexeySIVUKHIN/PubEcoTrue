from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .forms import *
from .models import *
from django.urls import reverse, reverse_lazy

from .permissions import IsAdminOrReadOnly
from .serializers import SensorDataSerializer
from .utils import DataMixin
from rest_framework import generics, status

menu = [
        {'title': "Новости", 'url_name': 'news'},
        {'title': "Статьи", 'url_name': 'articles'},
        {'title': "Оставить обращение", 'url_name': 'add_appeal'},
        {'title': "Состояние атмосферы", 'url_name': 'about'},
]

def index(request):
    news_page = news.objects.all()
    context = {'news_page': news_page,
               'menu': menu,
               'title': 'Главная страница'
    }
    return render(request, 'appeal/index.html', context = context)

def pageNotFound(request, exception):
    return render(request, 'appeal/404.html', {'menu': menu, 'title': 'Страница не найдена'})

def permissionDenied(request, exception):
    return render(request, 'appeal/403.html', {'menu': menu, 'title': 'Недостаточно прав'})

def About(request):
    return render(request, 'appeal/about.html', {'menu': menu, 'title': 'Состояние атмосферы'})

def Sensor1(request):
    return render(request, 'appeal/sensor1.html', {'menu': menu, 'title': 'Улица Громобоя, Иваново'})

class NewsList(ListView):
    paginate_by = 4
    model = news
    template_name = 'appeal/news.html'
    context_object_name = 'news_page'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        context['menu'] = menu

        return context

    def get_queryset(self):
        return news.objects.filter(is_published=True)

class ArticlesList(ListView):
    paginate_by = 4
    model = articles
    template_name = 'appeal/articles.html'
    context_object_name = 'articles_page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи'
        context['menu'] = menu
        return context

    def get_queryset(self):
        return articles.objects.filter(is_published=True)


def Appeal(request):
    if request.user.is_anonymous:
        return HttpResponse('''<h1>Пожалуйста, авторизуйтесь!</h1><br><a href='/'>На главную</a>''')
    else:
        if request.method == 'POST':
            form = AddAppealForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse('''<h1>Ваше обращение принято!</h1><br><a href='/'>На главную</a>''')
        else:
            form = AddAppealForm()
        return render(request, 'appeal/appeal.html', {'form': form, 'menu': menu,
                                                      'title': 'Обращение о нарушении '
                                                               'природоохранного законодательства'})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'appeal/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'appeal/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

def show_news(request, news_slug):
    post = get_object_or_404(news, slug=news_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'appeal/post.html', context=context)


def show_articles(request, articles_slug):
    post = get_object_or_404(articles, slug=articles_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'appeal/post.html', context=context)



from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import SensorDataSerializer


class SensorDataView(viewsets.ViewSet):
    serializer_class = SensorDataSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def create(self, request):
        data = request.data
        sensordatavalues = data.get('sensordatavalues')
        sensor_data = {}

        for value in sensordatavalues:
            value_type = value.get('value_type')
            value = value.get('value')
            sensor_data[value_type] = value
        sensor_data["esp8266id"] = data.get('esp8266id')
        serializer = self.serializer_class(data=sensor_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def list(self, request):
        sensor_data = SensorData2.objects.all()
        serializer = self.serializer_class(sensor_data, many=True)
        return Response(serializer.data)

class SensorDataLastList(ListView):
    paginate_by = 4
    model = SensorData2
    template_name = 'appeal/SensorDataLastList.html'
    context_object_name = 'SensorDataLastList'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Последние значения'
        context['menu'] = menu
        return context

    def get_queryset(self):
        return SensorData2.objects.all()