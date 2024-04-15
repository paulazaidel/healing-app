from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.messages import constants, add_message


def login(request):
    if request.method == "GET":
        return HttpResponse("Login")


def create(request):
    if request.method == "GET":
        return render(request, "create.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        users = User.objects.filter(username=username)

        if users.exists():
            add_message(request, constants.ERROR, "Usuário já existe")
            return redirect("create")

        if password != confirm_password:
            add_message(request, constants.ERROR, "As senhas não coincidem")
            return redirect("create")

        if len(password) < 6:
            add_message(
                request, constants.ERROR, "A senha deve possuir pelo menos 6 caracteres"
            )
            return redirect("create")

        try:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect("login")
        except:
            add_message(request, constants.ERROR, "Erro ao criar usuário")
            return redirect("create")
