# Generated by Django 3.0.6 on 2020-05-30 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_article_is_main_in_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(db_column='category_no', default=14, on_delete=django.db.models.deletion.SET_DEFAULT, to='main_app.Category'),
        ),
    ]
