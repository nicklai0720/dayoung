from django.db import models

# Create your models here.
class FormingMachine(models.Model):

    def __str__(self):
        return self.item_name + '_' + self.time_zone + '_' + self.machine_code

    item_name = models.CharField(max_length=200)
    machine_code = models.CharField(max_length=200)
    time_zone = models.CharField(max_length=200)
    actual_time = models.FloatField()
    modulus = models.IntegerField(null=True)
    per_mins = models.FloatField()
    output = models.IntegerField()
    capacity = models.IntegerField()


class DailyReport(models.Model):
    WORK_TIME_CHOICES = [
        ('A', 'A班'),
        ('B', 'B班'),
    ]

    MATERIAL_CHOICES = [
        ('PET', 'PET'),
        ('PP', 'PP'),
    ]

    def __str__(self):
        return str(self.form_machine) + '_' + str(self.date)

    form_machine = models.ForeignKey(FormingMachine, on_delete=models.CASCADE)
    material = models.CharField(max_length=200, choices=MATERIAL_CHOICES, null=True)
    work_time = models.CharField(max_length=1, choices=WORK_TIME_CHOICES, null=True)
    date = models.DateField(null=True)
    price = models.IntegerField(null=True)
    total_produce = models.IntegerField(null=True)
    error_amounts = models.IntegerField(null=True)
    produce_time_hour = models.IntegerField(null=True)
    produce_time_mins = models.IntegerField(null=True)
    turn_on_speed_per_mins = models.FloatField(null=True)
    employee =  models.CharField(max_length=200, null=True)
    total_amounts_produce = models.FloatField(default=0)
    error_amounts_percentage = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)
    produce_time = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    achieve_percentage = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    reasonable_produce = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    reasonable_produce_percentage = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)

    def calculate_produce(self, *args, **kwargs):
        if self.total_produce is not None and self.form_machine is not None:
            self.total_amounts_produce = self.total_produce * self.form_machine.output
        super(DailyReport, self).save(*args, **kwargs)

    def calculate_percentage(self, *args, **kwargs):
        if self.error_amounts is not None and self.total_amounts_produce is not None:
            self.error_amounts_percentage = self.error_amounts / (self.error_amounts + self.total_amounts_produce) * 100
        super(DailyReport, self).save(*args, **kwargs)

    def calculate_time(self, *args, **kwargs):
        if self.produce_time_hour is not None and self.produce_time_mins is not None:
            self.produce_time = self.produce_time_hour + self.produce_time_mins / 60
        super(DailyReport, self).save(*args, **kwargs)

    def calculate_achievement(self, *args, **kwargs):
        if self.total_produce is not None and self.form_machine.capacity is not None:
            self.achieve_percentage = self.total_produce / self.form_machine.capacity * 100
        super(DailyReport, self).save(*args, **kwargs)

    def calculate_reasonable(self, *args, **kwargs):
        if self.turn_on_speed_per_mins is not None and self.produce_time is not None:
            self.reasonable_produce = self.turn_on_speed_per_mins * self.produce_time * 60 / self.form_machine.output
        super(DailyReport, self).save(*args, **kwargs)

    def calculate_reasonable_percentage(self, *args, **kwargs):
        if self.total_produce is not None and self.reasonable_produce is not None:
            self.reasonable_produce_percentage = self.total_produce / self.reasonable_produce * 100
        super(DailyReport, self).save(*args, **kwargs)


