from django.shortcuts import render
from webapp.models import Propostas, CustomUser, Aluno, Orientador

#pagina principal
def aluno_home_view (request):
    #propostas = Propostas.objects.all()
    #print(propostas)
    #return render(request, "aluno/main_aluno.html")

    propostas = Propostas.objects.all()
    alunos = Aluno.objects.all()
    users = CustomUser.objects.all()
    #para receber as propostas criadas pelo orientador atual
    user=Aluno.objects.get(admin_id=request.user.id)
    return render(request, "aluno/main_aluno.html", {'propostas':propostas, 'alunos':alunos, 'users':users}) 

def aluno_info (request):
    return render(request, "aluno/info.html")

#pagina principal
def admin_home(request):
    # para contar o numero de users
    countTotal = CustomUser.objects.count()
    countOrient = CustomUser.objects.filter(user_type="2").count()
    countAluno = CustomUser.objects.filter(user_type="3").count()
    users = CustomUser.objects.all()
    context = {
        'countTotal':countTotal,
        'countOrient':countOrient,
        'countAluno':countAluno,
        'users':users,
    }
    return render(request, "admin/main_admin.html", context)

def list_all_proposta_view (request): 
    users = CustomUser.objects.all()
    propostas = Propostas.objects.all()
    return render(request, "aluno/list_proposta.html", {'propostas':propostas, 'users':users}) 

def list_proposta_view(request, proposta_id):
    users = CustomUser.objects.all()
    proposta=Propostas.objects.get(id=proposta_id)
    return render(request, "aluno/detail_proposta.html", {"proposta": proposta, 'users':users})