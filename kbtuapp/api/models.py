from django.db import models

# Create your models here.
class Info(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Photo(models.Model):
    photo = models.ImageField()
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='photos')