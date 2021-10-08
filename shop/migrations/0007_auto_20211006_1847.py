# Generated by Django 3.2.2 on 2021-10-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_home_homes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_cover_img', models.ImageField(upload_to='seting_image/')),
                ('small_cover_img', models.ImageField(upload_to='seting_image/')),
                ('cover_title', models.CharField(default='null', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Section1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section1_img', models.ImageField(upload_to='seting_image/')),
                ('section1_desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section2_title', models.CharField(max_length=30)),
                ('section2_desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Homes',
        ),
    ]