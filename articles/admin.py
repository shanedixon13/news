from django.contrib import admin

from articles.models import Category
from .models import Article, Category


admin.site.register(Article)
admin.site.register(Category)
