# Generated by Django 3.1.3 on 2023-08-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230815_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=5.0),
        ),
    ]