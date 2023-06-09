# Generated by Django 4.2 on 2023-05-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_billingaddress_province'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='apartment_address',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='country',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='amphur',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='tambol',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='zip',
            field=models.CharField(max_length=5),
        ),
    ]
