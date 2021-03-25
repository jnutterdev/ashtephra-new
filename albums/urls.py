from django.urls import path
from .views import AlbumListView, AboutPageView, HomePageView

urlpatterns = [
    path('albums/', AlbumListView.as_view(), name="albums"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('', HomePageView.as_view(), name="home"),
]