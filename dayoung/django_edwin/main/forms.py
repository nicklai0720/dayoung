from django import forms
from .models import DailyReport

class ItemForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = ['form_machine','material','date','work_time','price','total_produce',
        'error_amounts','turn_on_speed_per_mins','produce_time_hour','produce_time_mins',
        'employee']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': '格式yyyy-mm-dd'}),
        }
        labels = {
            'form_machine': '品名與機台',
            'material': '材質',
            'date': '日期',
            'work_time': '班別',
            'price': '售價',
            'total_produce': '成型數量',
            'error_amounts': '不良數',
            'turn_on_speed_per_mins': '開機速率',
            'produce_time_hour': '實際投入時數',
            'produce_time_mins': '實際投入分鐘',
            'employee': '機台人員'
        }
