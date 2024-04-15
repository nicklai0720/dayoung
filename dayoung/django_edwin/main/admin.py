from django.contrib import admin
from .models import FormingMachine, PrintingMachine

# Register your models here.
admin.site.register(FormingMachine)
admin.site.register(PrintingMachine)