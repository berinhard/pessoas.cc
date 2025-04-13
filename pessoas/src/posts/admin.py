from django.contrib import admin

from src.posts.models import NewPoemsCategorypost as CategoryPost
from src.posts.models import NewPoemsCategory as Category
from src.posts.models import NewPoemsPost as Post


class CategoryPostInline(admin.TabularInline):
    model = CategoryPost
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['author']
    search_fields = ['title']
    readonly_fields = ['created_at']
    prepopulated_fields = {'slug': ['title']}
    exclude = ['author_username', 'author_fullname']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [CategoryPostInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
