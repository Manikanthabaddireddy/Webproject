
from rest_framework import serializers
from .models import Web_Model,Remainder_Model

class WebSer(serializers.ModelSerializer):
    class Meta:
        model=Web_Model
        fields='__all__'

class RemSer(serializers.ModelSerializer):
    class Meta:
        model=Remainder_Model
        fields='__all__'