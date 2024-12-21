from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Favourites

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class UserRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class FavouritesSerializer(ModelSerializer):
    class Meta:
        model = Favourites
        fields = '__all__'
        