from rest_framework import serializers
from .models import Computer


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ['computer_name', 'processor', 'gpu', 'motherboard', 'ram']
