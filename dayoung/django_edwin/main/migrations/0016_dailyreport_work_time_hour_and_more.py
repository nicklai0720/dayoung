# Generated by Django 4.1 on 2024-04-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_dailyreport_error_amounts_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreport',
            name='work_time_hour',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='work_time_mins',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='work_time',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=10),
        ),
    ]