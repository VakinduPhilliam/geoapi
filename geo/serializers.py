from rest_framework import serializers
from .models import Polygon, ServiceArea, Provider
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PolygonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polygon
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    polygons = PolygonSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = ServiceArea
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = Provider
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                username=validated_data['username']
                )
            
            user.set_password(validated_data['password'])
            user.save()
            
            Token.objects.create(user=user)
            
            return user


