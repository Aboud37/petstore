# Generated by Django 3.2.2 on 2021-08-04 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20210804_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='author',
            new_name='user',
        ),
    ]
