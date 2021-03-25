from django.shortcuts import render
from rest_framework import generics
from albums.models import Album
from .serializers import AlbumSerializer
# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
