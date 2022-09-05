from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получаем текущую страницу и передаем ее в контекст
    # также передаем в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as csvfile:
        page_number = int(request.GET.get('page', 1))
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        paginator = Paginator(reader, 10)
        page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }

    return render(request, 'stations/index.html', context)
