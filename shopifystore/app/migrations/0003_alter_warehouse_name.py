# Generated by Django 4.0 on 2022-04-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_warehouse_product_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
