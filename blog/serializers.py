from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username','password')

        def validate_password(self, value):
            try:
                validate_password(value)
            except ValidationError as e:
                raise serializers.ValidationError(e.messages)
            
        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password']
            )
            return user










class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'