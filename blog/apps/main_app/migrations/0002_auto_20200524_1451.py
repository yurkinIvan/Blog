# Generated by Django 3.0.6 on 2020-05-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_description',
            field=models.CharField(max_length=150, verbose_name='Краткое описание статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='img/default_images/default.jpg', upload_to='img/articles'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=30, verbose_name='Название статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_main_article',
            field=models.BooleanField(default=False, verbose_name='Главная статья(всего 3 места)'),
        ),
    ]
