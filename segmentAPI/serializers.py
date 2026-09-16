from rest_framework import serializers
from .models import Canvas

class PortSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source='source.port', read_only=True, allow_null=True)
    target = serializers.CharField(source='target.port', read_only=True, allow_null=True)

    class Meta:
        model = Canvas
        fields = ['port', 'value', 'source', 'target']