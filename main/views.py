from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def demand(request):
    return render(request, 'main/Demand.html', {'title': 'Востребованность',})


def geography(request):
    return render(request, 'main/geography.html', {'title': 'География', })


def skills(request):
    return render(request, 'main/skills.html', {'title': 'Навыки', })


def latest_vacancies(request):
    return render(request, 'main/latest vacancies.html', {'title': 'Последние вакансии', })