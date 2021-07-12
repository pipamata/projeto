from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename=view_func.__module__
        user=request.user

        # se o user estiver autenticado
        if user.is_authenticated:
            # utilizador do tipo 1 -> admin
            if user.user_type == "1":
                    # dar permissao para interagir com estas páginas
                    if modulename == "webapp.views_admin":
                        pass
                    elif modulename == "webapp.views":
                        pass
                    else:
                        # página principal do admin
                        return HttpResponseRedirect(reverse("admin_home"))

            # utilizador do tipo 2 -> docente orientador
            elif user.user_type == "2":
                    # dar permissao para interagir com estas páginas
                    if modulename == "webapp.views_orientador":
                        pass
                    elif modulename == "webapp.views":
                        pass
                    else:
                        # página principal do docente orientador
                        return HttpResponseRedirect(reverse("orientador_home"))

            # utilizador do tipo 3 -> aluno
            elif user.user_type == "3":
                    # dar permissao para interagir com estas páginas
                    if modulename == "webapp.views_aluno":
                        pass
                    elif modulename == "webapp.views":
                        pass
                    else:
                        # página principal do aluno
                        return HttpResponseRedirect(reverse("aluno_home"))
            
            else:
                if modulename == "webapp.views":
                        pass
                else:
                    return HttpResponseRedirect(reverse("show_login"))

        # user não autenticado pode aceder a estas páginas
        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or request.path == reverse("register") or request.path == reverse("register_save"):
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))