from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Album
# Create your views here.
class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BaseView(TemplateView):
    template_name = 'base.html'

