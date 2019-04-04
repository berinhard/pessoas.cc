# Generated by Django 2.1.7 on 2019-04-03 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190402_0916'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='authgroup',
            table='old_auth_group',
        ),
        migrations.AlterModelTable(
            name='authgrouppermissions',
            table='old_auth_group_permissions',
        ),
        migrations.AlterModelTable(
            name='authpermission',
            table='old_auth_permission',
        ),
        migrations.AlterModelTable(
            name='authuser',
            table='old_auth_user',
        ),
        migrations.AlterModelTable(
            name='authusergroups',
            table='old_auth_user_groups',
        ),
        migrations.AlterModelTable(
            name='authuseruserpermissions',
            table='old_auth_user_user_permissions',
        ),
        migrations.AlterModelTable(
            name='djangoadminlog',
            table='old_django_admin_log',
        ),
        migrations.AlterModelTable(
            name='djangocontenttype',
            table='old_django_content_type',
        ),
        migrations.AlterModelTable(
            name='djangosession',
            table='old_django_session',
        ),
        migrations.AlterModelTable(
            name='djangosite',
            table='old_django_site',
        ),
        migrations.AlterModelTable(
            name='poemscategory',
            table='old_poems_category',
        ),
        migrations.AlterModelTable(
            name='poemscategorypost',
            table='old_poems_categorypost',
        ),
        migrations.AlterModelTable(
            name='poemspost',
            table='old_poems_post',
        ),
        migrations.AlterModelTable(
            name='southmigrationhistory',
            table='old_south_migrationhistory',
        ),
    ]