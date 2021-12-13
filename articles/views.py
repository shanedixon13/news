from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model=Article
    template_name="article_list.html"

class FrontPageListView(LoginRequiredMixin, ListView):
    model=Article
    template_name="front_page.html"

class LocalListView(LoginRequiredMixin, ListView):
    model=Article
    template_name="local.html"

class SportsListView(LoginRequiredMixin, ListView):
    model=Article
    template_name="sports.html"

class TravelListView(LoginRequiredMixin, ListView):
    model=Article
    template_name="travel.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name ="article_detail.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name="article_new.html"
    fields=['title', 'body',]

    def form_valid(self, form):
        user=self.request.user
        form.instance.author = user
        form.instance.category = user.department
        return super().form_valid(form)


class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name="article_edit.html"
    fields=['title', 'body', 'image',]

    def test_func(self):
        obj=self.get_object()
        return obj.author.id == self.request.user.id


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name="article_delete.html"
    success_url=reverse_lazy("article_list")

    def test_func(self):
        obj=self.get_object()
        return obj.author.id == self.request.user.id

