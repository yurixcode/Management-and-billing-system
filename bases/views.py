
# Django

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from django.urls import reverse_lazy

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    raise_exception=False
    redirect_field_name='redirect_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        # Si el usuario está logueado, le mostrará que no tiene permisos
        # Sino lo está, lo mandará a /login
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'
    
class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    template_name='bases/sin_privilegios.html'