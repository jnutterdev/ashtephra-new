from django.urls import path
from .views import AlbumListView, AboutPageView, HomePageView, BaseView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('albums/', AlbumListView.as_view(), name="albums"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('', BaseView.as_view(), name="home"),
]