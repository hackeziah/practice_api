from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from practice_app.models import Blog, Author, Entry

# Blog Serializer


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'name', 'tagline')

# Author Serializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email')

# Entry Serializer


class EntrySerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(many=True)
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Entry
        fields = ('blog', 'headline', 'body_text', 'pub_date', 'mod_date',
                  'author_name', 'number_of_comments', 'number_of_pingbacks', 'rating')

    def get_author_name(self, obj):
        return obj.author_name()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# Login Serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
