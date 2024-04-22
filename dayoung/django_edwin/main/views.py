from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse
from .models import FormingMachine, DailyReport
from itertools import chain
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
import locale
from datetime import datetime
from django.contrib import messages


# Create your views here.
# show all machine code in DB, example: 202, 203, 401...
def machine_list(request):
    item_list_form = FormingMachine.objects.values('machine_code').distinct()
    item_list = list(item_list_form)
    
    context = {
        'item_list': item_list,
        'range_list': ['2', '3', '4', '5'],
    }
    return render(request, 'main/index.html', context)


def detail(request, machine_code):
    # current_month = datetime.now().month
    forming_machine = get_list_or_404(FormingMachine, machine_code=machine_code)

    # 從請求中獲取選定的年月值
    selected_month = request.GET.get('start')

    # 如果沒有選定的年月值，則默認為當前月份
    if not selected_month:
        selected_month = datetime.now().strftime('%Y-%m')

    # 解析年月值，並從中獲取年份和月份
    year, month = selected_month.split('-')
    
    # 從 DailyReport 中獲取相應機器代碼的數據
    machine_data_list = DailyReport.objects.filter(
        form_machine__machine_code=machine_code,
        date__year=year,
        date__month=month).order_by('date')

    # 檢查是否存在數據，如果沒有則重定向到另一個頁面
    if not machine_data_list.exists():
        messages.warning(request, f"機器代碼 {machine_code} 目前沒有{month}月份相關數據，請新增!")
        return redirect('dayoung:add')

    total_boxes = sum(report.total_produce for report in machine_data_list)
    total_amounts = sum(report.total_amounts_produce for report in machine_data_list)
    total_prices = sum(report.price for report in machine_data_list)
    total_errors = sum(report.error_amounts for report in machine_data_list)
    error_percentage = total_errors / (total_amounts + total_errors) * 100
    total_reasonable_produces = sum(report.reasonable_produce for report in machine_data_list)
    achieve_rate = total_boxes / total_reasonable_produces * 100

    context = {
        'machine_data_list': machine_data_list,
        'machine_code': machine_code,
        'total_boxes': total_boxes,
        'total_amounts': total_amounts,
        'total_prices': total_prices,
        'total_errors': total_errors,
        'error_percentage': error_percentage,
        'total_reasonable_produces':total_reasonable_produces,
        'achieve_rate': achieve_rate,
    }
    
    return render(request, 'main/machine_code.html', context)


def add(request):
    form = ItemForm(request.POST or None)
 
    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)  # 先保存表單但不提交到數據庫
        instance.calculate_produce()  # 計算並更新 total_amounts_produce
        instance.calculate_percentage() # 計算不良率
        instance.calculate_time() # 計算時數
        instance.calculate_achievement() # 計算達成率
        instance.calculate_reasonable() # 計算開機時間合理產能
        instance.calculate_reasonable_percentage() # 計算開機時間達成率
        instance.save()
        return redirect('dayoung:machine_list')
    
    return render(request, 'main/add-report-form.html', {'form': form})

