from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main_page(request):
    title_h1 = 'Главная страница'
    context = {
        'title_h1': title_h1
    }
    return render(request, 'main_page.html', context)


def games(request):
    title_h1 = 'Игры'
    games_all = Game.objects.all()    # получили записи из таблицы Game
    main_page = '/main_page'
    context = {
        'title_h1': title_h1,
        'games_all': games_all,
        'main_page': main_page
    }
    return render(request, 'games.html', context)


def basket(request):
    title_h1 = 'Корзина'
    basket_empty = 'Извините, ваша корзина пуста'
    main_page = '/main_page'
    context = {
        'title_h1': title_h1,
        'basket_empty': basket_empty,
        'main_page': main_page
    }
    return render(request, 'basket.html', context)


# Проверить здесь пути для регистрации
def sign_up_by_html(request):
    buyers = Buyer.objects.all()    # получили записи из таблицы Buyer
    info = {}
    if request.method == 'POST':
        # Получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        for buyer in buyers:
            if username == buyer.name:
                info['error'] = 'Пользователь уже существует'
                break
        else:
            if password == repeat_password:
                # Проверим выводом в консоли, что данные от пользователя обработаны и получены сервером (для себя)
                print(f'Username: {username}. Password: {password}. Repeat_password: {repeat_password}. Age: {age}.')
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                info['error'] = 'Пароли не совпадают'
    return render(request, 'registration_page.html', {'info': info})
