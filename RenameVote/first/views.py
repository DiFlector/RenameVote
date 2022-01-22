import datetime
from django.shortcuts import render
from first.forms import RegistrationForm
from first.forms import AuthorizationForm
from first.models import ClientModel


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
    correct_password = True
    correct_login = True
    success = True

    if request.method == 'POST':
        form = AuthorizationForm(request.POST)

        if not form.is_valid():
            success = False
        elif not database.exists_with_login(form.data['login']):
            correct_login = False
        elif database.get_client_with_login(form.data['login']).password != form.data['password']:
            correct_password = False
        else:
            pass
            # TODO
    else:
        form = AuthorizationForm()

    context = {
        'correct_password': correct_password,
        'correct_login': correct_login,
        'success': success,
        'form': form,
    }

    return render(request, 'autorization.html', context)


def registration_page(request):
    success = True
    correct_password = True
    new = True

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if not form.is_valid():
            success = False
        elif ClientModel.objects.exists_client_with_login(form.data['login']):
            new = False
        elif form.data['password'] != form.data['confirm_password']:
            correct_password = False
        else:
            client = ClientModel(name=form.data['name'], phone=form.data['phone'],
                                 login=form.data['login'], email=form.data['email'])

            if client.is_valid():
                client.save()
                print('Client was successfully added')
            else:
                success = False
    else:
        form = RegistrationForm()

    context = {
        'correct': success,
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
