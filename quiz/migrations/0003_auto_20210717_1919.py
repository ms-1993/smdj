# Generated by Django 3.1 on 2021-07-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210717_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=10000),
        ),
    ]
