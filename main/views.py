from django.shortcuts import render
from .models import Demand


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',})


def demand(request):
    demand = Demand.objects.order_by('id')
    return render(request, 'main/Demand.html', {'title': 'Востребованность', 'demand': demand})


def geography(request):
    #tasks = Task.objects.order_by('id')
    return render(request, 'main/geography.html', {'title': 'География'})


def skills(request):
    #tasks = Task.objects.order_by('id')
    return render(request, 'main/skills.html', {'title': 'Навыки', })


def latest_vacancies(request):
    #tasks = Task.objects.order_by('id')
    return render(request, 'main/latest vacancies.html', {'title': 'Последние вакансии', })