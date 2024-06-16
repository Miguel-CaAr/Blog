from django.contrib import admin
from .models import Category

@admin.register(Category)
class Categories(admin.ModelAdmin):
  list_display = ['title', 'published']