# Generated by Django 3.1 on 2020-08-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pooshak', '0007_auto_20200819_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportset',
            name='inventory',
            field=models.IntegerField(default=0, verbose_name='تعداد موجودی'),
        ),
    ]
