# Generated by Django 4.1 on 2024-04-19 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_dailyreport_work_time_hour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyreport',
            name='work_time_hour',
        ),
        migrations.RemoveField(
            model_name='dailyreport',
            name='work_time_mins',
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='produce_time_hour',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='produce_time_mins',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='produce_time',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='work_time',
            field=models.CharField(choices=[('A', 'A班'), ('B', 'B班')], max_length=1, null=True),
        ),
    ]
