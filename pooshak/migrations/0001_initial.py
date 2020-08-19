# Generated by Django 3.1 on 2020-08-12 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='SportSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('brand', models.CharField(max_length=50, verbose_name='برند')),
                ('jens', models.CharField(max_length=50, verbose_name='جنس پارچه')),
                ('tarh', models.CharField(choices=[('S', 'ساده'), ('T', 'طرح دار')], max_length=1, verbose_name='طرح پارچه')),
                ('form', models.CharField(choices=[('M', 'معمولی'), ('A', 'آزاد')], max_length=2, verbose_name='فرم لباس')),
                ('kolah', models.IntegerField(choices=[('0', 'بدون کلاه'), ('1', 'کلاهدار')], verbose_name='کلاه')),
                ('pic', models.ImageField(upload_to='SportSet', verbose_name='تصویر')),
                ('size', models.ManyToManyField(to='pooshak.Size', verbose_name='سایز')),
            ],
            options={
                'verbose_name': 'ست گرمکن و شلوار ورزشی',
                'verbose_name_plural': 'ست گرمکن و شلوار ورزشی',
            },
        ),
    ]
