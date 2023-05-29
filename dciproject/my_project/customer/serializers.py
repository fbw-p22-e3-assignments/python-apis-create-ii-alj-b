#new - whole script added by instructor
from rest_framework import serializers 
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator
from datetime import date
from .models import Customer      

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['pk', 'name', 'email', 'created']

