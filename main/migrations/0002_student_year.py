# Generated by Django 3.1.5 on 2021-01-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
