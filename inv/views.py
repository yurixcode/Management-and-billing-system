# Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

# Mixins
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Decoradores
from django.contrib.auth.decorators import login_required, permission_required

# Vistas Django
from django.views import generic

# Modelos
from .models import Categoria, SubCategoria, Marca, Unidad_medida, Producto

# Vistas Heredadas
from bases.views import SinPrivilegios

# Forms
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, \
    ProductoForm


# CATEGORÍA

class CategoriaView(SinPrivilegios,\
    generic.ListView):
    permission_required = 'inv.view_categoria'

    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'


class CategoriaNew(SinPrivilegios, SuccessMessageMixin,\
    generic.CreateView):
    permission_required='inv.add_categoria'

    model = Categoria
    template_name='inv/categoria_form.html'
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url=reverse_lazy('inv:categoria_list')

    success_message="Categoría creada satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, SinPrivilegios,\
    generic.UpdateView):
    permission_required='inv.change_categoria'

    model = Categoria
    template_name='inv/categoria_form.html'
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url=reverse_lazy('inv:categoria_list')

    success_message="Categoría actualizada satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required='inv.delete_categoria'

    model=Categoria
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy('inv:categoria_list')
    



# SUB CATEGORÍA

class SubCategoriaView(SinPrivilegios,\
    generic.ListView):
    permission_required = 'inv.view_subcategoria'

    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    

class SubCategoriaNew(SinPrivilegios, generic.CreateView):
    permission_required='inv.add_subcategoria'

    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class=SubCategoriaForm
    success_url=reverse_lazy('inv:subcategoria_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(SinPrivilegios, generic.UpdateView):
    permission_required='inv.change_subcategoria'

    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class=SubCategoriaForm
    success_url=reverse_lazy('inv:subcategoria_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class SubCategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required='inv.delete_subcategoria'

    model=SubCategoria
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy('inv:subcategoria_list')




# MARCA

class MarcaView(SinPrivilegios,\
    generic.ListView):
    permission_required= 'inv.view_marca'

    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    permission_required= 'inv.add_marca'

    model = Marca
    template_name='inv/marca_form.html'
    context_object_name = 'obj'
    form_class=MarcaForm
    success_url=reverse_lazy('inv:marca_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    permission_required= 'inv.change_marca'

    model = Marca
    template_name='inv/marca_form.html'
    context_object_name = 'obj'
    form_class=MarcaForm
    success_url=reverse_lazy('inv:marca_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not marca:
        return redirect('inv:marca_list')

    if request.method == 'GET':
        contexto={'obj':marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.error(
            request,
            '{} Inactivada'.format(
                str(marca),
                )
            )
        return redirect('inv:marca_list')

    return render(request, template_name, contexto)




# UM

class UMView(SinPrivilegios, generic.ListView):
    permission_required='inv.view_um'

    model = Unidad_medida
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'


class UMNew(SinPrivilegios, generic.CreateView):
    permission_required='inv.add_um'
    
    model = Unidad_medida
    template_name='inv/UM_form.html'
    context_object_name = 'obj'
    form_class=UMForm
    success_url=reverse_lazy('inv:um_list')


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class UMEdit(SinPrivilegios, generic.UpdateView):
    permission_required='inv.change_um'

    model = Unidad_medida
    template_name='inv/um_form.html'
    context_object_name = 'obj'
    form_class=UMForm
    success_url=reverse_lazy('inv:um_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_um', login_url='bases:sin_privilegios')
def UM_inactivar(request, id):
    um = Unidad_medida.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not um:
        return redirect('inv:um_list')

    if request.method == 'GET':
        contexto={'obj':um}

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect('inv:um_list')

    return render(request, template_name, contexto)



# Producto

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name='inv/producto_form.html'
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url=reverse_lazy('inv:producto_list')
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name='inv/producto_form.html'
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url=reverse_lazy('inv:producto_list')
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def Producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not producto:
        return redirect('inv:producto_list')

    if request.method == 'GET':
        contexto={'obj':producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect('inv:producto_list')

    return render(request, template_name, contexto)
