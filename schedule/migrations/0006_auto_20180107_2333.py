# Generated by Django 2.0 on 2018-01-07 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20180107_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycle',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cycle',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
