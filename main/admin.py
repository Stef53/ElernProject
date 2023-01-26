from django.contrib import admin
from .models import Demand

@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ['year', 'salaryPerYear', 'amountOfVacancies', 'managerSalaryPerYear', 'managerAmountOfVacancies']
    list_editable = ['salaryPerYear', 'amountOfVacancies', 'managerSalaryPerYear', 'managerAmountOfVacancies']
    ordering = ['-year']


