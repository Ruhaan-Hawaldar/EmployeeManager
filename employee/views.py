# Testing Neon workflow trigger
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# CREATE + READ
# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, 'employee/employee_list.html', {'employees': employees})

# ..........................................................................
def employee_list(request):
    membership = request.GET.get('membership')
    coaching = request.GET.get('coaching')
    
    employees = Employee.objects.all()

    if membership:
        employees = employees.filter(membership_type=membership)

    if coaching:
        employees = employees.filter(coaching_category=coaching)

    return render(request, 'employee/employee_list.html', {'employees': employees})

# .........................................................................

def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_form.html', {'form': form})

# UPDATE
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_form.html', {'form': form})

# DELETE
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})


from django.shortcuts import render, redirect
from .forms import AttendanceForm
from .models import Attendance

def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'employee/mark_attendance.html', {'form': form})

def attendance_list(request):
    records = Attendance.objects.all().order_by('-date')
    return render(request, 'employee/attendance_list.html', {'records': records})



# ..........................

from django.core.paginator import Paginator
from django.http import HttpResponse
import csv
from .models import Attendance

def attendance_list(request):
    records = Attendance.objects.all().order_by('-date')

    # Filters
    search = request.GET.get('search')
    date_filter = request.GET.get('date')
    status_filter = request.GET.get('status')

    if search:
        records = records.filter(employee__name__icontains=search)
    if date_filter:
        records = records.filter(date=date_filter)
    if status_filter:
        records = records.filter(status=status_filter)

    # Pagination
    paginator = Paginator(records, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/attendance_list.html', {
        'page_obj': page_obj,
        'paginator': paginator,
        'records': page_obj.object_list,
    })


def export_attendance_excel(request):
    records = Attendance.objects.all().order_by('-date')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=attendance.csv'

    writer = csv.writer(response)
    writer.writerow(['Employee', 'Date', 'Status'])

    for record in records:
        writer.writerow([record.employee.name, record.date, record.status])

    return response
