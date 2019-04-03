# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class PoemsCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=110)
    created_at = models.DateTimeField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'old_poems_category'


class PoemsCategorypost(models.Model):
    post_raw_id = models.IntegerField(default=0)
    cat_raw_id = models.IntegerField(default=0)
    position = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'old_poems_categorypost'


class PoemsPost(models.Model):
    author_userrname = models.CharField(max_length=200, default='')
    author_fullname = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=300)
    resource_html = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'old_poems_post'


class SouthMigrationhistory(models.Model):
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'old_south_migrationhistory'
