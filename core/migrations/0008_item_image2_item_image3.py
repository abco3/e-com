# Generated by Django 4.2 on 2023-04-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200510_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image2',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='image3',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
