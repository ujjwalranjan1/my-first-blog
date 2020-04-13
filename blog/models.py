from django.conf import settings
from django.db import models #these models are defined in django.db.models.fields, but for convenience they’re imported into django.db.models;
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):#function/method
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#when we call __str__ this will return title
        return self.title
