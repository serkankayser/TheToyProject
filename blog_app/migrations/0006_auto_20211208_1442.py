# Generated by Django 3.1 on 2021-12-08 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20211208_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='edited_by',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_edited_by', to='blog_app.writer'),
        ),
    ]
