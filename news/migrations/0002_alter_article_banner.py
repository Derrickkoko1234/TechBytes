# Generated by Django 4.1.1 on 2023-06-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banners'),
        ),
    ]