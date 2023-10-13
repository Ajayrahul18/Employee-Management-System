
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .filters import *
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def emp_list(request):
    employee = Employee.objects.all()
    return render(request, 'emp_list.html', {'employee': employee})

def add_emp(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'add_emp.html', {'form': form})

def delete_emp(request):
    employee = Employee.objects.all()
    return render(request, 'delete_emp.html', {'employee': employee})

def remove_emp(request, id):
    Employee.objects.get(id=id).delete()
    return redirect('index')

def filter_emp(request):
    employee = Employee.objects.all()
    emp_filter = EmployeeFilter(request.GET, queryset=Employee.objects.all())
    employee = emp_filter.qs
    return render(request, 'filter_emp.html', {'emp_filter': emp_filter, "employee": employee})

