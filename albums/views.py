from django.shortcuts import render
from .models import Album
# Create your views here.
class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'

    