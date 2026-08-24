# blog/models.py
from django.db import models

class Post(models.Model):  # Must match 'Post' exactly
    title = models.CharField(max_length=200)
    # ...
