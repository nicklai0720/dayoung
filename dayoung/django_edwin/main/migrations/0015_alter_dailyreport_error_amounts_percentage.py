# Generated by Django 4.1 on 2024-04-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_dailyreport_error_amounts_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='error_amounts_percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]