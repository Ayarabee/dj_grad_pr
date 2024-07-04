from rest_framework import serializers
from .models import *



class RespiratoryDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespiratoryDetection
        fields = '__all__'