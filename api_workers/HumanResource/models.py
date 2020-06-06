from django.db import models


# Create your models here.
class Department():
    department_id = 0
    name = ''
    url = ''


class Job():
    job_id = 0
    name = ''


class Worker():
    emploee_id = 0
    first_name = ''
    last_name = ''
    email = ''
    phone_number = ''
    hire_date = ''
    job_id = []
    salary = 0
    commission_pct = 0
    manager_id = ''
    department_id = ''
    picture = ''
    name = ''
    flag = 1
    manager_name = ''
    emploee_json = ''
    department_name = ''


