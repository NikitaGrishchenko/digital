# Generated by Django 3.2.8 on 2021-11-12 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='dont_show_the_post',
            new_name='dont_show_the_project',
        ),
    ]
