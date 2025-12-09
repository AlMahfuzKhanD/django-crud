from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees})

# CREATE
def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees.index')
    else:
        form = EmployeeForm()

    return render(request, 'employees/form.html', {'form': form})

#Update
def edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees.index')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/form.html', {'form': form})
# Delete
def delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employees.index')