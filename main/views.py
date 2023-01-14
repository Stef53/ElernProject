from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def demand(request):
    return render(request, 'main/Demand.html')


def geography(request):
    return render(request, 'main/geography.html')


def skills(request):
    return render(request, 'main/skills.html')


def latest_vacancies(request):
    return render(request, 'main/latest vacancies.html')