from django.db import models


class Category(models.Model):
  title = models.CharField(max_length=255, null=False)
  slug = models.SlugField(max_length=255, unique=True)
  published = models.BooleanField(null=False)
  
  def __str__(self):
    return self.title
  