from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.static import serve as mediaserve
from publiceco import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('addappeal/', Appeal, name='add_appeal'),
    path('articles/', ArticlesList.as_view(), name='articles'),
    path('news/', NewsList.as_view(), name='news'),
    path('about/', About, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('news/<slug:news_slug>/', show_news, name='news'),
    path('articles/<slug:articles_slug>/', show_articles, name='articles'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('api/v1/sensorlist/', SensorDataView.as_view({'post': 'create', 'get': 'list'}), name='sensorlist'),
    path('4664744/', SensorDataLastList.as_view(), name='4664744'),
    path('sensor-data-latest/', sensor_data_latest, name='sensor_data_latest'),
    path('data/', data_view, name='data_view'),
]

handler404 = pageNotFound
handler403 = permissionDenied


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]