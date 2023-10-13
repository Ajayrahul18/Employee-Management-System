from django import forms
from django.forms import ModelForm
from .models import *


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ["name"]

class DepartmentForm(ModelForm):
    class Meta:
        models = Role
        fields = ["name", "location",]

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name", "sec_name", "dept", "salary", "role", "bonus", "phone"]
        