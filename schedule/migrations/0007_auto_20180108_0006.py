# Generated by Django 2.0 on 2018-01-08 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20180107_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleday',
            name='weekday',
            field=models.CharField(choices=[('Mon', 'Понедельник'), ('Tue', 'Вторник'), ('Wed', 'Среда'), (
                'Thu', 'Четверг'), ('Fri', 'Пятница'), ('Sat', 'Суббота'), ('Sun', 'Воскресение')], max_length=5),
        ),
    ]
