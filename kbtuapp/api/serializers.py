from rest_framework.serializers import ModelSerializer
from .models import Info, Photo

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'photo']

class InfoSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)
    class Meta:
        model = Info
        fields = ['id', 'text', 'created_at', 'photos']
