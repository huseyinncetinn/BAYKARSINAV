# Generated by Django 4.2.4 on 2023-08-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykarapp', '0002_kategori_kategoriresim'),
    ]

    operations = [
        migrations.AddField(
            model_name='iha',
            name='fiyat',
            field=models.IntegerField(null=True),
        ),
    ]