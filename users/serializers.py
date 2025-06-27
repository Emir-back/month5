from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ConfirmationCode
import random

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = False
        user.save()

        code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        ConfirmationCode.objects.create(user=user, code=code)
        print(f"Код подтверждения: {code}") 
        return user

class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
            confirmation = ConfirmationCode.objects.get(user=user)
        except (User.DoesNotExist, ConfirmationCode.DoesNotExist):
            raise serializers.ValidationError("Пользователь или код не найден")

        if confirmation.code != data['code']:
            raise serializers.ValidationError("Неверный код")

        user.is_active = True
        user.save()
        confirmation.delete()
        return data
