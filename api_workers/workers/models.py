from django.db import models


class Department(models.Model):
    department_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.department_id) + ' - ' +self.name


class Job(models.Model):
    job_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.job_id) + ' - ' +self.name


class Worker(models.Model):
    emploee_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    hire_date = models.CharField(max_length=50)
    job_id = models.ManyToManyField(Job)
    salary = models.IntegerField()
    commission_pct = models.FloatField()
    manager_id =  models.IntegerField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    # picture = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='')
    def __str__(self):
        return str(self.emploee_id) + ' - ' + self.first_name + ' ' + self.last_name
