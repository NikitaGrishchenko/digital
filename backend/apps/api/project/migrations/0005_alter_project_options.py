# Generated by Django 3.2.8 on 2021-12-08 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_dont_show_the_post_project_dont_show_the_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проект'},
        ),
    ]
