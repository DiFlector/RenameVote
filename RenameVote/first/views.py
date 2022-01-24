import datetime
from django.shortcuts import render
from first.forms import RegistrationForm
from first.forms import AuthorizationForm
from first.models import ClientModel, VotingModel
from first.forms import VotingForm
from django.shortcuts import redirect

def index_page(request):
    context = {}

    return render(request, 'index.html', context)


def questions_page(request):
    success = True

    if request.method == 'POST':
        form = VotingForm(request.POST)

        if not form.is_valid():
            success = False
        else:
            voting_owner_id = request.COOKIES.get('user_id')

            if voting_owner_id is None:
                voting_owner_id = -1

            voting = VotingModel(type=form.data['type'], owner_id=voting_owner_id,
                                 name=form.data['name'], date=datetime.datetime.now())

            if not voting.is_valid():
                success = False
            else:
                print('Voting successfully added')
                voting.save()

    else:
        form = VotingForm()

    context = {
        'success': success,
        'form': form
    }

    return render(request, 'questions.html', context)


def gay_page(request):
    context = {}

    return render(request, 'Kostyagay.html', context)


def authorization_page(request):
    correct_password = True
    correct_login = True
    success = True

    if request.method == 'POST':
        form = AuthorizationForm(request.POST)

        if not form.is_valid():
            success = False
        elif not ClientModel.objects.exists_client_with_login(form.data['login']):
            correct_login = False
        elif ClientModel.objects.get_client_with_login(form.data['login']).password != form.data['password']:
            correct_password = False
        else:
            print('User with login ' + form.data['login'] + ' successfully authorized')
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
    success = True

    if request.method == 'POST':
        pass
    else:
        success = False

    context = {
        'success': success,
    }

    return render(request, 'profile.html', context)


def news_page(request):
    context = {}

    return render(request, 'news.html', context)


def calc_page(request):
    return render(request, 'calculator.html')
