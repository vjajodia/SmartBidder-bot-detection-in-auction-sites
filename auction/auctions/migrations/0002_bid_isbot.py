# Generated by Django 4.1.3 on 2022-11-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='isBot',
            field=models.BooleanField(default=False),
        ),
    ]