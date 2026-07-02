"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('writers/', views.writers, name='writers'),
    path('writers/Hemingway/', views.writers_hemingway, name='Hemingway'),
    path('writers/Hemingway/<str:slug>/', views.hemingway_books, name='hemingway_book'),
    path('writers/Shakespeare/', views.writers_shakespeare, name='Shakespeare'),
    path('writers/Shakespeare/<str:slug>/', views.shakespeare_books, name='shakespeare_book'),
    path('writers/<path:anything>/', views.writers),

    path('books/', views.books, name='books'),
    path('books/<int:place>/', views.book_place, name="book_place"),

    path('<path:anything>/', views.home)
]
