# Generated by Django 3.2.6 on 2022-02-28 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان برگه')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=25, unique=True)),
                ('description', models.TextField(max_length=5000, verbose_name='محتوا')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('status', models.CharField(choices=[('pub', 'منتشر شده'), ('dra', 'پیش نویس'), ('del', 'زباله دان')], max_length=3, verbose_name='وضعیت انتشار')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
