# Generated by Django 3.0.6 on 2020-05-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyser', '0010_remove_analysisjob_jwt_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisjob',
            name='jwt_token',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='analysisjob',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
