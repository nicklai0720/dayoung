# Generated by Django 4.1 on 2024-04-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_dailyreport_reasonable_produce_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='reasonable_produce',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=10),
        ),
    ]
