# Generated by Django 2.0.6 on 2018-07-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20180701_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproduct',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, unique=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, unique=True),
        ),
    ]