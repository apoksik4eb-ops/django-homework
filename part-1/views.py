from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, "home.html")

def show_datetime(request):
    current_datetime = datetime.now()
    return render(request, 'datetime.html', {'datetime': current_datetime})

def multiplication_table(request):
    size = 10
    headers = list(range(1, size + 1))
    rows = []
    for i in headers:
        cells = [i * j for j in headers]
        rows.append((i, cells))
    return render(request, 'table.html', {
        'headers': headers,
        'rows': rows,
    })

from datetime import datetime, timedelta

def programmer_day(request):
    year = datetime.now().year
    programmer_day = datetime(year, 1, 1) + timedelta(days=255)
    return render(request, 'programmer.html', {'date': programmer_day})