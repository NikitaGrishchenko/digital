# Generated by Django 3.2.8 on 2021-12-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, null=True, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('appeal', models.TextField(null=True, verbose_name='Обращение')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
