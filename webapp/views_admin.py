from django.contrib import messages
from webapp.models import Aluno, CustomUser, Orientador, Propostas
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

#pagina principal
def admin_home(request):
    # para contar o numero de users
    countTotal = CustomUser.objects.count()
    countOrient = CustomUser.objects.filter(user_type="2").count()
    countAluno = CustomUser.objects.filter(user_type="3").count()
    countProp = Propostas.objects.count()
    users = CustomUser.objects.all()
    context = {
        'countTotal':countTotal,
        'countOrient':countOrient,
        'countAluno':countAluno,
        'countProp':countProp,
        'users':users,
    }
    return render(request, "admin/main_admin.html", context)

#adicionar orientador
def add_orientador_view(request):
    return render(request, "admin/add_orientador.html")

def add_orient_view(request):
    if request.method!='POST':
        return HttpResponse("Method not Allowed")
    else:
        username=request.POST.get("username")
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        password=request.POST.get("password")
        email=request.POST.get("email")

        user=CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)
        user.save()
        messages.success(request, "Adicionou Orientador com sucesso")
        return HttpResponseRedirect("/add_orientador")

#adicionar aluno
def add_aluno_view(request):
    return render(request, "admin/add_aluno.html")

def add_aluno_save_view(request):
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
        return HttpResponseRedirect("/add_aluno")

# ver orientadores
def manage_orientador_view(request):
    orientadores=Orientador.objects.all()
    return render(request, "admin/manage_orientador.html", {'orientadores':orientadores})

# ver alunos
def manage_aluno_view(request):
    alunos=Aluno.objects.all()
    return render(request, "admin/manage_aluno.html", {'alunos':alunos})

# editar orientador
def edit_orientador_view(request, orientador_id):
    orientador=Orientador.objects.get(admin=orientador_id)
    return render(request, "admin/edit_orientador.html", {"orientador": orientador})

def edit_orient_save_view(request):
    if request.method!='POST':
        return HttpResponse("Method not Allowed")
    else:
        orientador_id=request.POST.get("orientador_id")
        username=request.POST.get("username")
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        email=request.POST.get("email")

        user=CustomUser.objects.get(id=orientador_id)
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()

        orientador_model=Orientador.objects.get(admin=orientador_id)
        orientador_model.save()

        messages.success(request, "Editou com sucesso")
        return HttpResponseRedirect("/edit_orientador/"+orientador_id) 

# editar aluno
def edit_aluno_view(request, aluno_id):
    aluno=Aluno.objects.get(admin=aluno_id)
    return render(request, "admin/edit_aluno.html", {"aluno": aluno})

def edit_aluno_save_view(request):
    if request.method!='POST':
        return HttpResponse("Method not Allowed")
    else:
        aluno_id=request.POST.get("aluno_id")
        username=request.POST.get("username")
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        email=request.POST.get("email")

        user=CustomUser.objects.get(id=aluno_id)
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()

        aluno_model=Aluno.objects.get(admin=aluno_id)
        aluno_model.save()

        messages.success(request, "Editou com sucesso")
        return HttpResponseRedirect("/edit_aluno/"+aluno_id) 
    
def list_all_proposta_view (request):
    users = CustomUser.objects.all()
    propostas = Propostas.objects.all()
    return render(request, "admin/list_proposta.html", {'propostas':propostas, 'users':users}) 

def list_proposta_view(request, proposta_id):
    users = CustomUser.objects.all()
    proposta=Propostas.objects.get(id=proposta_id)
    return render(request, "admin/detail_proposta.html", {"proposta": proposta, 'users':users})
