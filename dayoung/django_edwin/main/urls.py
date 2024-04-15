from . import views
from django.urls import path

urlpatterns = [
    # /main/ show all machine code in DB
    path('', views.machine_list, name='machine_list'),
    # /main/'machine_code'/ show specific machine_code table
    path('<int:item_id>', views.detail, name='detail'),
]