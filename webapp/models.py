from django.db import models
from  django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"Admin"),(2,"Orientador"),(3,"Aluno"))
    user_type=models.CharField(default=1, choices=user_type_data,max_length=10)

# model do admin
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects=models.Manager()

# model dos docentes orientadores
class Orientador(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects=models.Manager()

# model do aluno
class Aluno(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects=models.Manager()
    status=models.BooleanField(default=False)

# model das propostas
class Propostas(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=255)
    orientador_id=models.ForeignKey(Orientador, on_delete=models.CASCADE)
    aluno_id = models.ForeignKey(Aluno, on_delete=models.SET_NULL, blank=True, null=True)
    objetivos=models.TextField(default="")
    areas_trabalho=models.TextField(default="")
    tarefas=models.TextField(default="")
    requisitos=models.CharField(max_length=255)
    elem_avaliacao=models.TextField(default="")
    resultados=models.CharField(max_length=255)
    referencias=models.TextField(default="")
    objects=models.Manager()

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
           Admin.objects.create(admin=instance)

        if instance.user_type==2:
           Orientador.objects.create(admin=instance)
           
        if instance.user_type==3:
           Aluno.objects.create(admin=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admin.save()
    
    if instance.user_type==2:
        instance.orientador.save()
    
    if instance.user_type==3:
        instance.aluno.save()

