from django.db import models


class Post(models.Model):
    your_name = models.CharField(max_length=100)
