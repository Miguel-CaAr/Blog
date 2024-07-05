from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category
from cloudinary.models import CloudinaryField

class Post(models.Model):
  title = models.CharField(max_length=255, null=False)
  content = models.TextField(null=False)
  slug = models.SlugField(max_length=255, unique=True)
  # miniature = models.ImageField(upload_to='posts/images/')
  miniature = CloudinaryField('image', default='')
  created_at = models.DateTimeField(auto_now_add=True)
  published = models.BooleanField(null=False)
  user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
  category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
  
  def __str__(self):
    return self.title