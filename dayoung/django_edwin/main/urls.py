from . import views
from django.urls import path


app_name = 'dayoung'
urlpatterns = [
    # /main/ show all machine code in DB
    path('', views.machine_list, name='machine_list'),
    # /main/machine/'machine_code'/ show specific machine_code table
    path('machine/<int:machine_code>/', views.detail, name='detail'),
    # /main/machine/'machine_code'/add
    path('add/', views.add, name='add'),
]