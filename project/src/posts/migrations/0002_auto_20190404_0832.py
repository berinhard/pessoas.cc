# Generated by Django 2.2 on 2019-04-04 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newpoemscategory',
            options={'ordering': ['-created_at'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='newpoemscategorypost',
            options={'ordering': ['position'], 'verbose_name': 'Posts de Categoria'},
        ),
        migrations.AlterModelOptions(
            name='newpoemspost',
            options={'ordering': ['-created_at'], 'verbose_name': 'Postagem', 'verbose_name_plural': 'Postagens'},
        ),
    ]
