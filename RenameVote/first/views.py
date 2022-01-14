import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse


def index_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'aboutus.html')


def authorization_page(request):
    return render(request, 'autorization.html')


def contacts_page(request):
    return render(request, 'contacts.html')


def profile_page(request):
    return render(request, 'profile.html')


def questions_page(request):
    return render(request, 'questions.html')


def registration_page(request):
    return render(request, 'registration.html')
