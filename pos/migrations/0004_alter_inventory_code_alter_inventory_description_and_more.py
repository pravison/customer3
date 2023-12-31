# Generated by Django 4.2.4 on 2023-09-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_alter_inventory_actualpurchaseprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inventoryType',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='measurementUnit',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
