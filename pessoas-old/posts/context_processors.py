#coding:utf-8
from posts.models import NewPoemsCategory as Category
from posts.models import NewPoemsCategorypost as CategoryPost

def get_categories(request):
    cat_ids = CategoryPost.objects.values_list('category', flat=True)
    return {'categories': Category.objects.filter(id__in=cat_ids)}
