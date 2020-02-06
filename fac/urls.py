from django.urls import path

# Views
from .views import ClienteView, ClienteNew, ClienteEdit, clienteInactivar,\
    FacturaView, facturas,\
        ProductoView,\
        borrar_detalle_factura

from .reportes import imprimir_factura_recibo

urlpatterns = [
    # Clientes
    path('clientes/', ClienteView.as_view(), name='cliente_list'),
    path('clientes/new', ClienteNew.as_view(), name='cliente_new'),
    path('clientes/<int:pk>', ClienteEdit.as_view(), name='cliente_edit'),
    path('clientes/estado/<int:id>', clienteInactivar, name='cliente_inactivar'),

    # Facturas
    path('facturas/', FacturaView.as_view(), name='factura_list'),
    path('facturas/new', facturas, name='factura_new'),
    path('facturas/edit/<int:id>', facturas, name='factura_edit'),
    path('facturas/borrar-detalle/<int:id>', borrar_detalle_factura, name='factura_borrar_detalle'),

    # Producto
    path('facturas/buscar-producto', ProductoView.as_view(), name='factura_producto'),

    # Imprimir
    path('facturas/imprimir/<int:id>', imprimir_factura_recibo, name='factura_imprimir_one'),


]