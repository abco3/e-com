# Generated by Django 4.2 on 2023-05-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_payment_reciept_order_reciept'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='model',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
