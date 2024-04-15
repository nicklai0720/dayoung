from django.shortcuts import render
from django.http import HttpResponse
from .models import FormingMachine, PrintingMachine
from itertools import chain
# from django.template import loader
# from django.db.models import Count

# Create your views here.
# show all machine code in DB, example: 202, 203, 401...
def machine_list(request):
    item_list_form = FormingMachine.objects.values('machine_code').distinct()
    item_list_print = PrintingMachine.objects.values('machine_code').distinct()
    # print('show:', item_list_form)
    item_list = list(chain(item_list_form, item_list_print))
    
    context = {
        'item_list': item_list,
    }
    return render(request, 'main/index.html', context)

# 
def detail(request, item_id):
    return HttpResponse('item id: %s' % item_id)
