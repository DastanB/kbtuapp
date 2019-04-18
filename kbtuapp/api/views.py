from django.shortcuts import render
from .models import Info, Photo
from .serializers import InfoSerializer, PhotoSerializer

from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class InfoList(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoDetails(generics.RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class PhotoList(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetails(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer