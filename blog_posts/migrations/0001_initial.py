# Generated by Django 3.0.6 on 2020-08-09 18:04

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
            name='BlogPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, default='defaut.png', upload_to='')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=120)),
                ('video', models.CharField(default=False, max_length=3000)),
                ('content', models.TextField(blank=True, null=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_date', '-timestamp', '-updated'],
            },
        ),
    ]
