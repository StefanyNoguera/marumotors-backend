from rest_framework import serializers
from .models import Car, Autopart

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class AutopartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autopart
        fields = '__all__'
