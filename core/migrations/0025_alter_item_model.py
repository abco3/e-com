# Generated by Django 4.2 on 2023-05-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_category_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='model',
            field=models.CharField(choices=[('iPhone 12', 'iPhone 12'), ('iPhone 12 mini', 'iPhone 12 mini'), ('iPhone 12 Pro', 'iPhone 12 Pro'), ('iPhone 12 Pro Max', 'iPhone 12 Pro Max'), ('iPhone 13', 'iPhone 13'), ('iPhone 13 mini', 'iPhone 13 mini'), ('iPhone 13 Pro', 'iPhone 13 Pro'), ('iPhone 13 Pro Max', 'iPhone 13 Pro Max'), ('iPhone 14', 'iPhone 14'), ('iPhone 14 Plus', 'iPhone 14 Plus'), ('iPhone 14 Pro', 'iPhone 14 Pro'), ('iPhone 14 Pro Max', 'iPhone 14 Pro Max')], max_length=50, null=True),
        ),
    ]