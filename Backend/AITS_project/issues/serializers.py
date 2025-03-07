from rest_framework import serializers
from .models import Issue, Comment, Notification
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'role')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']

class IssueSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'issue_type', 'course_code', 'status', 'student', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['id', 'status', 'student', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user
        return super().create(validated_data)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'issue', 'message', 'is_read', 'created_at']
        read_only_fields = ['id', 'created_at']






