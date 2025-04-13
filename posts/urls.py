from django.urls import path

from posts.views import HomeIndexView

app_name = 'poems'

urlpatterns = [
    path('', HomeIndexView.as_view(), name='index'),
    # re_path(r'^todos/$', list_all, name='list_all'),
    # re_path(r'^aleatorio/$', random_post_view, name='random'),
    # re_path(r'^autor/(?P<author_username>[\w\d-]+)/$', list_by_author, name='list_by_author'),
    # re_path(r'^texto/(?P<post_slug>[\w\d-]+)/$', post_detail, name='post_detail'),
    # re_path(r'^categoria/(?P<category_slug>[\w\d-]+)/$', category_start, name='category'),
    # re_path(r'^categoria/(?P<category_slug>[\w\d-]+)/(?P<post_slug>[\w\d-]+)/$', post_category_detail, name='cat_post_detail'),
]
