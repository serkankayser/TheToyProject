# Generated by Django 3.1 on 2021-12-08 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_editor', models.BooleanField(default=False)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('edited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_edited_by', to='blog_app.writer')),
                ('written_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_written_by', to='blog_app.writer')),
            ],
        ),
    ]
