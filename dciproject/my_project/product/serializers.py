#new - whole script added by instructor
from rest_framework import serializers 
from rest_framework.validators import UniqueTogetherValidator
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'id', 'created', 'image', 'category']

        validators = [
            UniqueTogetherValidator(
                queryset=Product.objects.all(),
                fields=['name', 'image']
            )
        ]