from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    joining_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )

    class Meta:
        model = Employee
        # fields = ['name', 'email', 'department', 'joining_date']
        # .......................
        fields = ['name', 'email', 'department', 'joining_date', 'membership_type', 'coaching_category']
        # .......................
from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
