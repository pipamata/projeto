"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings

from django.conf.urls.static import static

# get the views from the app
from webapp import views, views_admin, views_aluno, views_orientador

urlpatterns = [
    path('', views.loginPage, name="show_login"),
    path('doLogin', views.logins, name="do_login"),
    
    path('register', views.register, name="register"),
    path('register_save', views.register_save, name="register_save"),
    
    path('get_user_details', views.GetUserDetails),
    
    path('logout_user', views.logout_user, name="logout"),

    path('accounts/', include('django.contrib.auth.urls')),

    # Admin ------------------------------------------------------------
    path('admin_home', views_admin.admin_home, name="admin_home"),

    path('add_orientador', views_admin.add_orientador_view, name="add_orientador"),
    path('add_orient_save', views_admin.add_orient_view, name="add_orient_save"),
    
    path('add_aluno', views_admin.add_aluno_view, name="add_aluno"),
    path('add_aluno_save', views_admin.add_aluno_save_view, name="add_aluno_save"),

    path('manage_orientador', views_admin.manage_orientador_view, name="manage_orientador"),
    path('manage_aluno', views_admin.manage_aluno_view, name="manage_aluno"),

    path('edit_orientador/<str:orientador_id>', views_admin.edit_orientador_view, name="edit_orientador"), 
    path('edit_orient_save', views_admin.edit_orient_save_view, name="edit_orient_save"),

    path('edit_aluno/<str:aluno_id>', views_admin.edit_aluno_view, name="edit_aluno"), 
    path('edit_aluno_save', views_admin.edit_aluno_save_view, name="edit_aluno_save"),
    
    path('list_all_proposta', views_admin.list_all_proposta_view, name="list_all_proposta"),
    path('list_proposta/<str:proposta_id>', views_admin.list_proposta_view, name="list_proposta"),

    # Orientador -------------------------------------------------------
    path('orientador_home', views_orientador.orientador_home_view, name="orientador_home"),
    
    path('add_proposta', views_orientador.add_proposta_view, name="add_proposta"),
    path('add_proposta_save', views_orientador.add_proposta_save_view, name="add_proposta_save"),
    
    path('orientador_list_all_proposta', views_orientador.list_all_proposta_view, name="orientador_list_all_proposta"),
    path('orientador_list_proposta/<str:proposta_id>', views_orientador.list_proposta_view, name="orientador_list_proposta"),
    
    path('atrib_aluno', views_orientador.atrib_aluno, name="atrib_aluno"),

    # Aluno ------------------------------------------------------------
    path('aluno_home', views_aluno.aluno_home_view, name="aluno_home"),
    
    path('aluno_list_all_proposta', views_aluno.list_all_proposta_view, name="aluno_list_all_proposta"),
    path('aluno_list_proposta/<str:proposta_id>', views_aluno.list_proposta_view, name="aluno_list_proposta"),
    
    path('aluno_info', views_aluno.aluno_info, name="aluno_info"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
