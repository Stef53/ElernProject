from django.db import models

class Demand(models.Model):
    year = models.IntegerField(default=2008)
    salaryPerYear = models.IntegerField(default=1)
    amountOfVacancies = models.IntegerField(default=1)
    managerSalaryPerYear = models.IntegerField(default=1)
    managerAmountOfVacancies = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.year} - {self.salaryPerYear} - {self.amountOfVacancies} - {self.managerSalaryPerYear} - {self.managerAmountOfVacancies}'



