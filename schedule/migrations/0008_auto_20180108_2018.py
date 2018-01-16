# Generated by Django 2.0 on 2018-01-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20180108_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='sets',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='scheduleday',
            name='weekday',
            field=models.SmallIntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (
                2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресение')]),
        ),
    ]
