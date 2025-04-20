from django.db import models
from datetime import date

# class Employee(models.Model):
#     DEPARTMENT_CHOICES = [
#         ('HR', 'Human Resources'),
#         ('IT', 'Information Technology'),
#         ('FIN', 'Finance'),
#         ('MKT', 'Marketing'),
#         ('OPS', 'Operations'),
#     ]

#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
#     joining_date = models.DateField()

#     def __str__(self):
#         return self.name

# ........................................

from django.db import models

# models.py

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('MKT', 'Marketing'),
        ('OPS', 'Operations'),
    ]

    MEMBERSHIP_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Elite', 'Elite'),
    ]

    COACHING_CHOICES = [
        ('Technical', 'Technical'),
        ('Soft Skills', 'Soft Skills'),
        ('Leadership', 'Leadership'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    joining_date = models.DateField()

    # New fields
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES, default='Basic')
    coaching_category = models.CharField(max_length=20, choices=COACHING_CHOICES, default='Technical')

    def __str__(self):
        return self.name




# ...................................

class Attendance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')],
        default='Present'
    )

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"