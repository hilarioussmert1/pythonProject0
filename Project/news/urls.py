from django.urls import path
from .views import (NewsList, NewDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete)

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewDetail.as_view(), name='news_detail'),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_create'),
    path('articles/create/', NewsCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='articles_delete'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('categories/<int:pk>', )
]
