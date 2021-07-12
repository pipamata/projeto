from django.shortcuts import render
from webapp.models import Propostas, CustomUser, Orientador, Aluno
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect

#pagina principal
def orientador_home_view (request):
    propostas = Propostas.objects.all()
    alunos = Aluno.objects.all()
    users = CustomUser.objects.all()
    #para receber as propostas criadas pelo orientador atual
    user=Orientador.objects.get(admin_id=request.user.id)
    count=Propostas.objects.filter(orientador_id=user.id).count()  
    return render(request, "orientador/main_orientador.html", {'propostas':propostas, 'count':count, 'alunos':alunos, 'users':users}) 

#atribuir proposta
def atrib_aluno(request):
    if request.method!='POST':
        return HttpResponse("Method not Allowed")
    else:
        # do formulario - proposta_id e username
        proposta=request.POST.get("proposta")
        username=request.POST.get("atribuir")
        
        user=CustomUser.objects.filter(username=username)[0]
        alunos=Aluno.objects.all()
        
        for aluno in alunos:
            if user.id == aluno.admin_id :
                resultado=aluno.id
        
        Propostas.objects.filter(id=proposta).update(aluno_id=resultado)
        return HttpResponseRedirect("/orientador_home")

#adicionar proposta
def add_proposta_view(request): 
    return render(request, "orientador/add_proposta.html")

#adicionar proposta
def add_proposta_save_view(request):
    orient_id = request.user.id
    user=Orientador.objects.get(admin_id=orient_id)

    if request.method!='POST':
        return HttpResponse("Method not Allowed")
    else:
        titulo=request.POST.get("titulo")
        objetivos=request.POST.get("objetivos")
        areas_trabalho=request.POST.get("areas")
        tarefas=request.POST.get("tarefas")
        requisitos=request.POST.get("requisitos")
        elem_avaliacao=request.POST.get("elementos")
        resultados=request.POST.get("resultados")
        referencias=request.POST.get("referencias")
        orient_id= user.id

        proposta=Propostas(titulo=titulo, objetivos=objetivos,areas_trabalho=areas_trabalho,tarefas=tarefas,requisitos=requisitos,elem_avaliacao=elem_avaliacao,resultados=resultados,referencias=referencias, orientador_id_id=orient_id)
        proposta.save()
        messages.success(request, "Adicionou Proposta com sucesso")
        return HttpResponseRedirect("/add_proposta")


def list_all_proposta_view (request): 
    users = CustomUser.objects.all()
    propostas = Propostas.objects.all()
    return render(request, "orientador/list_proposta.html", {'propostas':propostas, 'users':users}) 

def list_proposta_view(request, proposta_id):
    users = CustomUser.objects.all()
    proposta=Propostas.objects.get(id=proposta_id)
    return render(request, "orientador/detail_proposta.html", {"proposta": proposta, 'users':users})