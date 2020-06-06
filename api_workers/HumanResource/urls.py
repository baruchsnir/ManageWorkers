from django.contrib import admin
from django.urls import path
from . import views
app_name='HumanResource'
urlpatterns = [
    path("", views.index, name="index"),
    path('workers_list/', views.workers_list, name='workers_list'),
    path('worker_detail/', views.worker_detail, name='worker_detail'),
    path('search/', views.searchworker, name='search'),
    path('eror/', views.eror, name='eror'),
    path('salarysummery/', views.SalarySummery, name='salarysummery'),
]


