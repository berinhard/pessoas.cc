#coding:utf-8
from src.posts.models import NewPoemsPost as Post
from src.posts.models import NewPoemsCategory as Category
from src.posts.models import NewPoemsCategorypost as CategoryPost

def get_categories(request):
    cat_ids = CategoryPost.objects.values_list('category', flat=True)
    return {'categories': Category.objects.filter(id__in=cat_ids)}
