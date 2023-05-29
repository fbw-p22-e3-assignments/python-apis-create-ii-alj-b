#new - whole script added by instructor
from rest_framework import serializers 
from rest_framework.validators import UniqueForYearValidator
from .models import Customer      

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['pk', 'name', 'email', 'created']

        validators = [
            UniqueForYearValidator(
                queryset=Customer.objects.all(),
                field='name',
                date_field='created'
            )
        ]