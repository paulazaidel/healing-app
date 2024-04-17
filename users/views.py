from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.messages import add_message, constants
from django.http import HttpResponse
from django.shortcuts import redirect, render


def logout(request):
    auth_logout(request)
    return redirect("users:login")


def login(request):
    if request.method == "GET":
        return render(request, "users_login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return HttpResponse("Usuário logado")

        add_message(request, constants.ERROR, "Usuário ou senha incorretos")
        return redirect("users:login")


def create(request):
    if request.method == "GET":
        return render(request, "users_create.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        users = User.objects.filter(username=username)

        if users.exists():
            add_message(request, constants.ERROR, "Usuário já existe")
            return redirect("users:create")

        if password != confirm_password:
            add_message(request, constants.ERROR, "As senhas não coincidem")
            return redirect("users:create")

        if len(password) < 6:
            add_message(
                request, constants.ERROR, "A senha deve possuir pelo menos 6 caracteres"
            )
            return redirect("users:create")

        try:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect("users:login")
        except:
            add_message(request, constants.ERROR, "Erro ao criar usuário")
            return redirect("users:create")
