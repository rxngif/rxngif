from django.shortcuts import render
from django.urls import path
from rest_framework import viewsets
from .models import Gif
from .serializers import GifSerializer

# Create your views here.
class GifViewSet(viewsets.ReadOnlyModelViewSet):
    """ GET all gifs """
    queryset = Gif.objects.all()
    serializer_class = GifSerializer