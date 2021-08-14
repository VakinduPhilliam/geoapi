from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Polygon, ServiceArea, Provider
from .serializers import ProviderSerializer, ServiceSerializer, PolygonSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    
    def destroy(self, request, *args, **kwargs):
        provider = Provider.objects.get(pk=self.kwargs["pk"])
        
        if not request.user == provider.created_by:
            raise PermissionDenied("You can not delete this provider.")
        
        return super().destroy(request, *args, **kwargs)

class ServiceAreaViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = ServiceArea.objects.all()
        provider_id = self.kwargs['provider_pk']
        queryset = queryset.filter(servicearea_owner=provider_id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        provider = Provider.objects.get(pk=self.kwargs["pk"])

        if not request.user == provider.created_by:
            raise PermissionDenied("You can not delete this service area.")
        
        return super().destroy(request, *args, **kwargs)

class PolygonViewSet(viewsets.ModelViewSet):
    serializer_class = PolygonSerializer

    def get_queryset(self):
        queryset = Polygon.objects.all()
        provider_id = self.kwargs['provider_pk']
        polygon_id = self.kwargs['polygon_pk']
        queryset = queryset.filter(provider=provider_id, servicearea_polygon=polygon_id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        provider = Provider.objects.get(pk=self.kwargs["pk"])
        
        if not request.user == provider.created_by:
            raise PermissionDenied("You can not delete this service area.")
        
        return super().destroy(request, *args, **kwargs)

class ServicesList(generics.ListAPIView):
    serializer_class = PolygonSerializer

    def get_queryset(self):
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')
        queryset = Polygon.objects.filter(lat=lat,lng=lng)    
        return queryset

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()
    
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

