# Generated by Django 3.2.6 on 2022-02-07 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='دسته بندی')),
                ('slug', models.SlugField(allow_unicode=True, max_length=20, unique=True, verbose_name='نامک')),
                ('display', models.BooleanField(default=True, verbose_name='نمایش')),
                ('position', models.IntegerField(default='0', verbose_name='جایگاه')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.category', verbose_name='دسته والد')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, max_length=20, unique=True, verbose_name='نامک')),
                ('description', models.TextField(max_length=1000, verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='images', verbose_name='تصویر شاخص')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('is_special', models.BooleanField(default=False, verbose_name='مقاله ویژه')),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده'), ('w', 'در انتظار تایید'), ('r', 'رد شده')], max_length=1, verbose_name='وضعیت')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ManyToManyField(related_name='articles', to='blog.Category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
                'ordering': ['-published'],
            },
        ),
    ]
