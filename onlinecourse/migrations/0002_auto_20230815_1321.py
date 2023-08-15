# Generated by Django 3.1.3 on 2023-08-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='text',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='choice text', max_length=550),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]