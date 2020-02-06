from rest_framework import serializers

# Models
from inv.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = '__all__'