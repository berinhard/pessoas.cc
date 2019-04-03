from django.db import models

from django.urls import reverse
from django.template.defaultfilters import slugify


class NewPoemsCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=110)
    created_at = models.DateTimeField()
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('poems:category', args=[self.slug])

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created_at']



class NewPoemsCategorypost(models.Model):
    post = models.ForeignKey('NewPoemsPost', models.DO_NOTHING)
    category = models.ForeignKey(NewPoemsCategory, models.DO_NOTHING)
    position = models.IntegerField()
    created_at = models.DateTimeField()

    def get_next_post(self):
        qs = NewPoemsCategorypost.objects.select_related('category', 'post')
        return qs.filter(position__gt=self.position, category=self.category).first()

    def get_previous_post(self):
        try:
            qs = NewPoemsCategorypost.objects.select_related('category', 'post')
            return qs.filter(position__lt=self.position, category=self.category).order_by('-position').latest('position')
        except self.DoesNotExist:
            return None

    def get_absolute_url(self):
        return reverse('poems:cat_post_detail', args=[self.category.slug, self.post.slug])

    class Meta:
        verbose_name = 'Post de Categoria'
        verbose_name = 'Posts de Categoria'
        ordering = ['position']


class NewPoemsPost(models.Model):
    author_userrname = models.CharField(max_length=200, default='')
    author_fullname = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=300)
    resource_html = models.TextField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_next_post(self):
        return NewPoemsPost.objects.filter(
            created_at__gt=self.created_at,
        ).order_by('created_at').first()

    def get_previous_post(self):
        return NewPoemsPost.objects.filter(
            created_at__lt=self.created_at,
        ).latest('created_at')

    def get_absolute_url(self):
        return reverse('poems:post_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-created_at']
