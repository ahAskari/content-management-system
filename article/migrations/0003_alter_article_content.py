# Generated by Django 4.2.7 on 2023-11-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=1000000),
        ),
    ]
