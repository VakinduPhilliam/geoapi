from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
    name = models.CharField(max_length=100) # Name of provider
    phone = models.CharField(max_length=100) # Phone number of provider
    language = models.CharField(max_length=100) # Language
    currency = models.CharField(max_length=100) # Created by
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) #  Provider credentials
    pub_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class ServiceArea(models.Model):
    servicearea_owner = models.ForeignKey(Provider, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Polygon(models.Model):
    servicearea_polygon = models.ForeignKey(ServiceArea, related_name='polygons', on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.CharField(max_length=100) # Lattitude coordinate
    lng = models.CharField(max_length=100) # Longitude coordinate
    
    class Meta:
        unique_together = ("lat", "lng")

