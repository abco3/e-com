# Generated by Django 4.1 on 2023-05-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_remove_category_image2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="banner",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
