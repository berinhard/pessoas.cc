from django.urls import path

from posts.views import *

app_name = 'poems'

urlpatterns = [
    path('', HomeIndexView.as_view(), name='index'),
    path('todos/', ListAllView.as_view(), name='list_all'),
    path('aleatorio/', random_post_view, name='random'),
    path('autor/<slug:author_username>/', ListByAuthorView.as_view(), name='list_by_author'),
    path('texto/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
    path('categoria/<slug:category_slug>/', category_start, name='category'),
    path('categoria/<slug:category_slug>/<slug:post_slug>/', post_category_detail, name='cat_post_detail'),
]
