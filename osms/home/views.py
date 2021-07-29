from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# home view
@login_required
def user_home(request):
    return render(request, 'home/index.html')


