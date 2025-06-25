from rest_framework import generics
from .models import Car, Autopart
from .serializers import CarSerializer, AutopartSerializer

# Cars
class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'

# Autoparts
class AutopartListView(generics.ListAPIView):
    queryset = Autopart.objects.all()
    serializer_class = AutopartSerializer

class AutopartDetailView(generics.RetrieveAPIView):
    queryset = Autopart.objects.all()
    serializer_class = AutopartSerializer
    lookup_field = 'id'
