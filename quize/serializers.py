from rest_framework import serializers
from .models import Quize

class QuizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quize
        fields = ('id', 'name', 'email', 'quiz_score', 'created_at', 'test_status', 'user_role')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        quize = Quize.objects.create(**validated_data)
        return quize
