from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Article(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_on=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])