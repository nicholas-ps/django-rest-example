from rest_framework import serializers
from .models import Lawyer
from django.contrib.auth.models import User

class ValidationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8,
        max_length=10
    )
    number = serializers.IntegerField()
    something = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()

    def get_something(self, data):
        return "Haiii"
    
    def get_token(self, data):
        return data["email"] + str(data["number"])

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password"
        )
        extra_kwargs = {
            "password" : {
                "write_only" : True
            }
        }

class LawyerSerializer(serializers.ModelSerializer):
    something = serializers.SerializerMethodField()
    user = UserSerializer()

    def get_something(self, obj):
        return "something"

    class Meta:
        model = Lawyer
        fields = (
            "id",
            "name",
            "age",
            "something",
            "user"
        )

    def create(self, validated_data):
        user_data = validated_data["user"]
        user = User.objects.create(
            username=user_data["username"],
            password=user_data["password"]
        )

        lawyer = Lawyer.objects.create(
            name=validated_data["name"],
            age=validated_data["age"],
            user = user
        )

        return lawyer

    def update(self, lawyer, validated_data):
        user_data = validated_data["user"]
        user = lawyer.user
        user.username = user_data["username"]
        user.set_password(user_data["password"])
        user.save()

        lawyer.name = validated_data["name"]
        lawyer.age = validated_data["age"]
        lawyer.save()

        return lawyer

