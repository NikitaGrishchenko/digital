# Generated by Django 3.2.8 on 2021-11-12 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='dont_show_the_post',
            new_name='dont_show_the_article',
        ),
    ]
