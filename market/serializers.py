from rest_framework import serializers
from .models import redmi, iphone

class redmiSerializer(serializers.ModelSerializer):
    class meta:
        model = redmi
        fields = ('model','year')

class iphoneSerializer(serializers.ModelSerializer):
    class meta:
        model = iphone
        fields = ('model', 'country')