# Generated by Django 2.0 on 2018-01-03 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0003_auto_20180102_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainDay',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=255)),
                ('mood', models.CharField(max_length=1)),
                ('program', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.ScheduleDay')),
            ],
        ),
        migrations.CreateModel(
            name='TrainResult',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField()),
                ('measure', models.CharField(default='kg', max_length=5)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('day', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='progress.TrainDay')),
                ('exercise', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='schedule.Exercise')),
            ],
        ),
    ]
