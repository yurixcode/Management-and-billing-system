from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Serializers
from .serializers import ProductoSerializer

# Models
from django.db.models import Q
from inv.models import Producto


class ProductoList(APIView):
    def get(self, request):
        prod = Producto.objects.all()
        data = ProductoSerializer(prod, many=True).data
        return Response(data)

# 'Serializar' se usa para mandar un response JSON :)
class ProductoDetalle(APIView):
    def get(self, request, codigo):
        prod = get_object_or_404(Producto, Q(codigo=codigo) | Q(codigo_barra=codigo))
        data = ProductoSerializer(prod).data
        return Response(data)