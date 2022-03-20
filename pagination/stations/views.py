from django.shortcuts import render, redirect
from django.urls import reverse
import os
from django.core.paginator import Paginator
import csv
from pathlib import Path
path = os.path.join(Path(__file__).parents[1], 'data-398-2018-08-30.csv')

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(path, encoding='utf8') as csvfile:
        records = csv.DictReader(csvfile)
        temp = []
        for srting_file in records:
            temp.append(srting_file['Name'])
            temp.append(srting_file['Street'])
            temp.append(srting_file['District'])
    print(temp)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(temp, 10)
    print(paginator)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': temp,
        'page': page
    }
    return render(request, 'stations/index.html', context)


with open(path, encoding='utf8') as csvfile:
    records = csv.DictReader(csvfile)
    temp = []
    for srting_file in records:
        temp.append([ srting_file['Name'], srting_file['Street'], srting_file['District']])
print(temp[0])


