# Generated by Django 3.0.6 on 2020-05-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_article_url', models.CharField(max_length=250)),
                ('source_article_title', models.CharField(max_length=250)),
                ('source_article_content', models.CharField(max_length=100000)),
            ],
        ),
    ]
