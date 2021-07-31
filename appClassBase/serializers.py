from rest_framework import serializers
from .models import Tech
from django.contrib.auth.models import User


class TechSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Tech
        fields = ['Address', 'code', 'name', 'mobile', 'owner']


class UserSerializer(serializers.ModelSerializer):
    tech = serializers.PrimaryKeyRelatedField(many=True, queryset=Tech.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tech']