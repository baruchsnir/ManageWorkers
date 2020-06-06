from django.contrib import admin
from django.urls import path,include
from . import views
# from . import models
from rest_framework import routers
router = routers.DefaultRouter()
router.register('jobs',views.JobView)
router.register('workers',views.WorkerView)
router.register('departments',views.DepartmentView)
urlpatterns = [
   path('',include(router.urls)),
]
