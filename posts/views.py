from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView

from posts.models import NewPoemsPost as Post
from posts.models import NewPoemsCategory as Category
from posts.models import NewPoemsCategorypost as CategoryPost
from django.shortcuts import render


class HomeIndexView(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()[:5]
