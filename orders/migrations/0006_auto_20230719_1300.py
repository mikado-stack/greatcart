# Generated by Django 3.1 on 2023-07-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20230719_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.CharField(max_length=50),
        ),
    ]