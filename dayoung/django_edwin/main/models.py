from django.db import models

# Create your models here.
class FormingMachine(models.Model):

    def __str__(self):
        return self.item_name + '_' + self.time_zone + '_' + self.machine_code

    item_name = models.CharField(max_length=200)
    machine_code = models.CharField(max_length=200)
    time_zone = models.CharField(max_length=200)
    actual_time = models.FloatField()
    modulus = models.IntegerField()
    per_mins = models.FloatField()
    output = models.IntegerField()
    capacity = models.IntegerField()


class PrintingMachine(models.Model):

    def __str__(self):
        return self.item_name + '_' + self.time_zone + '_' + self.machine_code

    item_name = models.CharField(max_length=200)
    machine_code = models.CharField(max_length=200)
    time_zone = models.CharField(max_length=200)
    actual_time = models.FloatField()
    per_mins = models.FloatField()
    output = models.IntegerField()
    capacity = models.IntegerField()

