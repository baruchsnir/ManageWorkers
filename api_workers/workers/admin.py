from django.contrib import admin
from .models import Job,Worker,Department

# Register your models here.
admin.site.register(Job)
admin.site.register(Worker)
admin.site.register(Department)
