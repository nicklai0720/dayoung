# Generated by Django 4.1 on 2024-03-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_formingmachine_time_zone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formingmachine',
            name='time_zone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='printingmachine',
            name='time_zone',
            field=models.CharField(max_length=200),
        ),
    ]
