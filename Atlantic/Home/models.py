from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Post(models.Model):

    date = models.DateTimeField(default=timezone.now)
    tittle = models.CharField(max_length=100)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    image_thumbnail = models.ImageField(upload_to='pics',default='newpost.png')
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})




