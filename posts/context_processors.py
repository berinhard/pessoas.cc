#coding:utf-8
from posts.models import NewPoemsCategory as Category
from posts.models import NewPoemsCategorypost as CategoryPost

def get_categories(request):
    return {'categories': Category.objects.filter(id__lte=7).exclude(id=3)}
