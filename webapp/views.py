from webapp.EmailBackEnd import EmailBackEnd
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from webapp.models import CustomUser

# Create your views here.

# abrir a pagina correspondente ao login
def register(request):
    return render(request,"register.html")

def register_save(request):
    if request.method!='POST':
        return HttpResponse("Method not Allowed")
    else:
        username=request.POST.get("username")
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        password=request.POST.get("password")
        email=request.POST.get("email")

        user=CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=3)
        user.save()
        messages.success(request, "Adicionou Aluno com sucesso")
        return HttpResponseRedirect("/register")

# abrir a pagina correspondente ao login
def loginPage(request):
    return render(request,"login.html")

# ao clicar no butao da form
def logins(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        print(user)
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("orientador_home"))
            else:
                return HttpResponseRedirect(reverse("aluno_home"))
        else:
            messages.error(request, "Invalid login details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("Email : "+request.user.email +" User Type :"+request.user.user_type)
    else:
        return HttpResponse("Por favor faça login")

# fazer logout
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")