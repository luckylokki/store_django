from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, SignInForm, UserProfileEdit, UserPasswordChange


@login_required(login_url='signin')
def user_profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'user_profile.html')


def signin_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect(reverse_lazy('product_list'))
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


def signup_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.create_user()
            return HttpResponseRedirect(reverse_lazy('signin'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='signin')
def signout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy("product_list"))


@login_required(login_url='signin')
def deactivate_user_view(request: HttpRequest) -> HttpResponse:
    request.user.is_active = False
    request.user.save()
    logout(request)
    return HttpResponseRedirect(reverse_lazy("signin"))


@login_required(login_url='signin')
def user_profile_edit(request: HttpRequest) -> HttpResponse:
    profile = request.user
    if request.method == 'POST':
        form = UserProfileEdit(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse_lazy('user_profile'))
    else:
        first_name = profile.first_name
        last_name = profile.last_name
        email = profile.email
        gender = profile.gender
        city = profile.city
        form = UserProfileEdit({"first_name": first_name, "last_name": last_name, "email": email,
                                "gender": gender, "city": city})
    return render(request, 'user_profile_edit.html', {'form': form})


@login_required(login_url='signin')
def change_profile_password(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserPasswordChange(request.POST, instance=request.user)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse_lazy('user_profile'))
    else:
        form = UserPasswordChange()
    return render(request, 'user_password_change.html', {'form': form})
