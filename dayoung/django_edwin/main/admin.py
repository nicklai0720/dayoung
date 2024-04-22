from django.contrib import admin
from .models import FormingMachine, DailyReport

# Register your models here.
admin.site.register(FormingMachine)
admin.site.register(DailyReport)