from rest_framework import serializers
from .models import Responsability

class ResponsabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsability
        fields = '__all__'
