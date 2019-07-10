from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def login(request):
    return render(request, 'login.html')

def validar_login(request):
    username = request
    password = request
