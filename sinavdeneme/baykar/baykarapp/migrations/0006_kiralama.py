# Generated by Django 4.2.4 on 2023-08-26 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baykarapp', '0005_remove_iha_kiralama'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kiralama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiralamaSaat', models.IntegerField()),
                ('kiralamaToplam', models.FloatField()),
                ('iha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykarapp.iha')),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
