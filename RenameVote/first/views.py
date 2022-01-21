import datetime
from django.shortcuts import render
from first.backend.Database import database
from first.forms import RegistrationForm


def index_page(request):
    context = {}

    return render(request, 'index.html', context)


def questions_page(request):
    context = {}

    return render(request, 'questions.html', context)


def Kostyagay_page(request):
    context = {}

    return render(request, 'Kostyagay.html', context)


def autorization_page(request):
    context = {}

    return render(request, 'autorization.html', context)


def registration_page(request):
    correct = False
    correct_password = True
    new = True
    form = None

    print('Registration')

    if request.method == 'POST':
        print('Post request')

        form = RegistrationForm(request.POST)
        client = database.create_client(form.data['name'], form.data['phone'], form.data['login'], form.data['email'])

        if database.exists_with_login(form.data['login']):
            new = False
        elif form.data['password'] != form.data['confirm_password']:
            correct_password = False
            print("Uncorrected password")
        elif client.check_client():
            database.add_client(client)
            correct = True
            print('Client was successfully added')
    else:
        form = RegistrationForm()
        correct = True

    context = {
        'correct': correct,
        'correct_password': correct_password,
        'new': new,
        'form': form
    }

    return render(request, 'registration.html', context)


def profile_page(request):
    context = {}

    return render(request, 'profile.html', context)


def news_page(request):
    context = {}

    return render(request, 'news.html', context)


def calc_page(request):
    return render(request, 'calculator.html')
