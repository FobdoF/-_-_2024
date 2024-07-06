import requests
from django.http import HttpResponse
from django.apps import AppConfig
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'



def index(request):
    return redirect('login')

@login_required
def login(request):
    return render(request, 'login.html')

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

def login(request):
    if request.method == 'POST':
        if request.POST.get("Enter"):
            full_name = request.POST.get('username')
            password = request.POST.get('password')
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s",
                               (str(full_name), str(password)))
                records = list(cursor.fetchall())
            return render(request, 'account.html', {'full_name': records[0][1]})
        elif request.POST.get("Reg"):
            return redirect("/registration/")
    return render(request, 'Enter.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        login = request.POST.get('login')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                           (str(name), str(login), str(password)))
        return redirect('/Enter/')
    return render(request, 'registration.html')



def my_view(request):
    # Определите URL API
    url = 'https://api.example.com'

    # Определите параметры запроса (если необходимо)
    params = {
        'param1': 'value1',
        'param2': 'value2'
    }

    # Определите заголовки запроса (если необходимо)
    headers = {
        'Authorization': 'Bearer ваш_токен_доступа',
        'Content-Type': 'application/json'
    }

    # Выполните запрос к API
    response = requests.get(url, params=params, headers=headers)

    # Обработайте ответ от API
    if response.status_code == 200:
        # Обработка успешного ответа
        data = response.json()
        # Ваш код обработки данных
        return render(request, 'my_template.html', {'data': data})
    else:
        # Обработка ошибки
        return HttpResponse('Ошибка при выполнении запроса: ' + str(response.status_code))


from django.db import connection


def get_data_from_database(view_func):
    def wrapper(request, *args, **kwargs):
        # Ваш код для выполнения запроса к базе данных
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s",
                           (request.POST.get('username'), request.POST.get('password')))
            records = cursor.fetchall()

        # Добавьте обработку полученных данных и передайте их в контекст шаблона
        context = {
            'full_name': records[0][1]
        }

        # Вызов исходной функции представления с обновленным контекстом
        return view_func(request, context, *args, **kwargs)

    return wrapper

@get_data_from_database
def login(request, context):
    if request.method == 'POST':
        if request.POST.get("login"):
            return render(request, 'account.html', context)
        elif request.POST.get("registration"):
            return redirect("/registration/")
    return render(request, 'login.html')

@get_data_from_database
def login(request, context):
    if request.method == 'POST':
        if request.POST.get("login"):
            return render(request, 'account.html', context)
        elif request.POST.get("registration"):
            return redirect("/registration/")
    return render(request, 'login.html')





