from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# def login(request):
#     return render(request, 'login.html')

# def validar_login(request):
#     usuario= request.POST['username']
#     password= request.POST['password']
#     usuarios = Login.objects.filter(usuario = usuario, password = password)
#     print(usuarios)
#     if usuarios is None:
#         print('entroo')
#         print(usuario)
#         messages.add_message(request, messages.INFO, 'EL USUARIO NO ESTA REGISTRADO')
#     else:
#         return render(request, 'menu.html')
@login_required
def menu(request):
    return render(request, 'menu.html')

# def Logout_view(request):
#     logout(request)
#     return render(request, 'login.html')
@login_required
def Lojanisima(request):
    return render(request, 'lojanisima/ruta_lojanisima.html')

@login_required
def Identiarte(request):
    return render(request, 'identiarte/ruta_identiarte.html')

@login_required
def Raices(request):
    return render(request, 'raice/ruta_raices.html')

@login_required
def Lojatur(request):
    return render(request, 'lojatur/lojatur.html')