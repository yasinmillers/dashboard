from rest_framework import serializers
from .models import User, Complaint
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ["id", "full_name", "email", "password"]

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ["complaint_id", "crime_type", "description", "status", "user"]
        read_only_fields = ["complaint_id", "status", "user"]