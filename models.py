from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    sec_name = models.CharField(max_length=200)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.sec_name}"

