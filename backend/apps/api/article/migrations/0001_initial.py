# Generated by Django 3.2.8 on 2021-10-21 09:29

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('preview', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Превью')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('date_of_publication', models.DateTimeField(verbose_name='Дата публикации')),
                ('dont_show_the_post', models.BooleanField(help_text='Есть флаг установлен, публикация будет скрыта', verbose_name='Не показывать публикацию?')),
                ('number_of_views', models.IntegerField(verbose_name='Количество просмотров публикации')),
                ('author', models.ManyToManyField(related_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['date_of_publication'],
            },
        ),
    ]
