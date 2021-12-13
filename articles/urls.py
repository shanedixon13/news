from django.urls import path
from .views import (
    ArticleListView,
    FrontPageListView,
    LocalListView,
    SportsListView,
    TravelListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleEditView,
    ArticleDeleteView
)

urlpatterns=[
    path('', ArticleListView.as_view(), name='article_list'),
    path('frontpage/', FrontPageListView.as_view(), name='front_page'),
    path('local/', LocalListView.as_view(), name='local'),
    path('sports/', SportsListView.as_view(), name='sports'),
    path('travel/', TravelListView.as_view(), name='travel'),
    path('<int:pk>/', ArticleDetailView.as_view(),name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete')
    ]