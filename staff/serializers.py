from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'fullname', 'username', 'password', 'is_deleted', 'create_date']
        extra_kwargs = {'password': {'write_only': True}}  # Hide password in responses
