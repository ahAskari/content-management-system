# Generated by Django 4.2.7 on 2023-11-25 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photo',
        ),
        migrations.CreateModel(
            name='ArticlePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(blank=True, null=True, upload_to='media/article')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article')),
            ],
            options={
                'db_table': 'photo',
            },
        ),
    ]
