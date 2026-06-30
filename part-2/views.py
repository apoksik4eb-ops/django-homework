from django.shortcuts import render

def home(request, anything=None):
    return render(request, "home.html")

def news(request, anything=None):
    return render(request, "news.html")

def management(request, anything=None):
    return render(request, "management.html")

def facts(request, anything=None):
    return render(request, "facts.html")

def contacts(request, anything=None):
    return render(request, "contacts.html")

def history(request, anything=None):
    return render(request, "history.html")

def history_people(request):
    return render(request, "history/history_people.html")

def history_photos(request):
    return render(request, "history/history_photos.html")