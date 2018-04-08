from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class BlogPost(models.Model):
    #id = pk (default in django)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, unique=True)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def owner(self):
        return self.user
    

    def get_api_url(self, request=None):
        return api_reverse("api-posts:post_rud", kwargs={'id':self.id}, request=request)