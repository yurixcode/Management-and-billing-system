# Django
from django.db import models
from django.contrib.auth.models import User

# App
from django_userforeignkey.models.fields import UserForeignKey

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)

    # FC = Fecha Creación - FM = Fecha Modificación
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)

    # UC = Usuario Creación - UM = Usuario Modificación
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract=True


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)

    # FC = Fecha Creación - FM = Fecha Modificación
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)

    # UC = Usuario Creación - UM = Usuario Modificación
    # uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # um = models.IntegerField(blank=True, null=True)
    uc = UserForeignKey(auto_user_add=True, related_name='+')
    um = UserForeignKey(auto_user=True, related_name='+')

    class Meta:
        abstract=True