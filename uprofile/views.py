from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


@login_required(login_url='signin')
def user_profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'user_profile.html')

def signin_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy("product_list"))
        else:
            return HttpResponseRedirect(reverse_lazy("signin"))
    return render(request, 'signin.html')


def signup_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username):
            context = {'message': 'User is exists'}
            return render(request, 'signup.html', context)

        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        if password != password_confirm:
            context = {'message': 'password do not match'}
        else:
            User.objects.create_user(username=username, password=password, email=email)
            return HttpResponseRedirect(reverse_lazy("signin"))
        return render(request, 'signup.html', context)

    return render(request, 'signup.html')


def signout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy("product_list"))


@login_required(login_url='signin')
def deactivate_user_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        request.user.is_active = False
        request.user.save()
        logout(request)
        return HttpResponseRedirect(reverse_lazy("signin"))
