# Generated by Django 2.2 on 2019-05-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190501_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpoemscategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='newpoemscategorypost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='newpoemspost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
