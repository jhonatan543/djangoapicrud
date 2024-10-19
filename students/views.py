from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Estudiante
from .serializers import EstudianteSerializer

# Listar todos los estudiantes o crear uno nuevo
class EstudianteListCreate(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

# Obtener, actualizar o eliminar un estudiante por su ID
class EstudianteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
