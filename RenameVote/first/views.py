import datetime
from django.shortcuts import render

from models import CalcHistory


context = {}
context['author'] = 'Костя ДИКИЙ BRUH'
context['status'] = 'Костя хочет кушать x2'


def index_page(request):



    return render(request, 'index.html', context)

def questions_page(request):



    return render(request, 'questions.html', context)

def Kostyagay_page(request):



    return render(request, 'Kostyagay.html', context)

def autorization_page(request):



    return render(request, 'autorization.html', context)

def registration_page(request):



    return render(request, 'registration.html', context)



def profile_page(request):


    return render(request, 'profile.html', context)

def news_page(request):



    return render(request, 'news.html', context)


def calc_page(request):
    a = request.GET.get('a', '29')
    b = request.GET.get('b', '23')
    c = int(a) + int(b)

    record = CalcHistory(date=datetime.datetime.now(),
                         first=a, second=b, result=c)
    record.save()

    data = CalcHistory.objects.all()


    context = {
        'first_value': a,
        'second_value': b,
        'result': c,
        'data': data
    }
    return render(request, 'calculator.html', context)
