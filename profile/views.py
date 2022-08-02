from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

user_data = {
    'id': 1,
    'username': 'lokki',
    'first_name': 'Vadim',
    'last_name': 'Prokopenko',
    'age': 36,
    'email': 'lokki@lokki.com',
    'university': 'Harvard University'
}


def user_profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'user_profile.html', user_data)

