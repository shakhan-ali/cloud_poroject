# Generated by Django 3.1 on 2020-11-09 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20201108_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]