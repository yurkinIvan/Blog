# Generated by Django 3.0.6 on 2020-06-09 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author_name',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
