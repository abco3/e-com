# Generated by Django 4.1 on 2023-05-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_payment_reciept"),
    ]

    operations = [
        migrations.RemoveField(model_name="payment", name="reciept",),
        migrations.AddField(
            model_name="order",
            name="reciept",
            field=models.FileField(null=True, upload_to="reciept"),
        ),
    ]
