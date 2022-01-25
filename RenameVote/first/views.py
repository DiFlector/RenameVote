import datetime
from django.shortcuts import render
from first.forms import RegistrationForm
from first.forms import AuthorizationForm
from first.models import ClientModel, VotingModel
from first.forms import VotingForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


def index_page(request):
    correct_password = True
    correct_login = True
    success = True

    print('Index')

    if request.method == 'POST':
        form = AuthorizationForm(request.POST)

        if not form.is_valid():
            success = False
            print('Index invalid form')
        elif not ClientModel.objects.exists_client_with_login(form.data['login']):
            correct_login = False
            print('Index no such client with login ' + form.data['login'])
        elif not ClientModel.objects.get_client_with_login(form.data['login']).check_password(form.data['password']):
            correct_password = False
            print('Index incorrect password')
        else:
            user = authenticate(request, username=form.data['login'], password=form.data['password'])
            login(request, user)
            print('User with login ' + form.data['login'] + ' successfully authorized')
            return redirect('/profile')
    else:
        form = AuthorizationForm()

    context = {
        'correct_password': correct_password,
        'correct_login': correct_login,
        'success': success,
        'form': form,
    }

    return render(request, 'index.html', context)


def questions_page(request):
    success = True

    if request.method == 'POST':
        form = VotingForm(request.POST)

        if not form.is_valid():
            success = False
        else:
            voting = VotingModel(type=form.data['type'], owner_id=-1,
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
    context = {}

    return render(request, 'autorization.html', context)


def registration_page(request):
    success = True
    correct_password = True
    new = True

    print('Registration page')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        print('Registration POST')

        if not form.is_valid():
            success = False
        elif ClientModel.objects.exists_client_with_login(form.data['login']):
            new = False
        elif form.data['confirm_password'] != form.data['password']:
            correct_password = False
        else:
            client = ClientModel.objects.create_user(username=form.data['login'],
                                                     name2=form.data['name'], phone2=form.data['phone'],
                                                     login2=form.data['login'], email2=form.data['email'])

            print('Try add client')

            client.set_password(form.data['password'])
            client.password2 = client.password

            if client.is_valid():
                client.save()
                print('Client was successfully added')
                user = authenticate(request, username=form.data['login'], password=form.data['password'])
                login(request, user)
                return redirect('profile')
            else:
                print('Registration fault')
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
    name = 'Anonymous'
    email = '-'
    phone = '-'

    if request.user.is_authenticated:
        name = ClientModel.objects.get_client_with_login(request.user.username).name2
        email = request.user.email
        phone = ClientModel.objects.get_client_with_login(request.user.username).phone2

    context = {
        'success': success,
        'name': name,
        'email': email,
        'phone': phone,
    }

    return render(request, 'profile.html', context)


def news_page(request):
    context = {}

    return render(request, 'news.html', context)


def calc_page(request):
    return render(request, 'calculator.html')
