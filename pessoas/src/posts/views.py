from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views.generic import ListView, DetailView
from django.template import RequestContext

from src.posts.models import NewPoemsPost as Post
from src.posts.models import NewPoemsCategory as Category
from src.posts.models import NewPoemsCategorypost as CategoryPost


class HomeIndexView(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()[:5]


class ListAllView(ListView):
    template_name = 'posts/list_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.objects.all()


class ListByAuthorView(ListView):
    template_name = 'posts/list_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        author_username = self.kwargs['author_username']
        #self.author = get_object_or_404(User, username=author_username)
        return Post.objects.filter(author_username=author_username)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'author': self.kwargs['author_username']})
        return context


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['next'] = self.object.get_next_post()
        context['previous'] = self.object.get_previous_post()
        return context


home_index = HomeIndexView.as_view()
list_all = ListAllView.as_view()
list_by_author = ListByAuthorView.as_view()
post_detail = PostDetailView.as_view()


def category_start(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    try:
        first_post = CategoryPost.objects.select_related('post').filter(category=category)[0]
    except IndexError:
        raise Http404

    cat_posts = CategoryPost.objects.select_related('post').filter(category=category)

    return render(request, 'posts/category_post.html', {'first_cat_post': first_post, 'cat_posts': cat_posts, 'category': category, })


def post_category_detail(request, category_slug, post_slug):
    category = get_object_or_404(Category, slug=category_slug)
    qs = CategoryPost.objects.select_related('category', 'post')
    cat_post = get_object_or_404(qs, category__slug=category_slug, post__slug=post_slug)
    context = {
        'category': category,
        'cat_post': cat_post,
        'next': cat_post.get_next_post(),
        'previous': cat_post.get_previous_post(),
    }
    return render(request, 'posts/cat_post_detail.html', context)


def random_post_view(request):
    post = Post.objects.all().order_by('?').first()
    return redirect(post.get_absolute_url())
