# Generated by Django 3.1 on 2023-06-14 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]