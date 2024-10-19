from django.urls import path
from .views import EstudianteListCreate, EstudianteRetrieveUpdateDestroy

urlpatterns = [
    path('estudiantes/', EstudianteListCreate.as_view(), name='estudiante-list'),
    path('estudiantes/<int:pk>/', EstudianteRetrieveUpdateDestroy.as_view(), name='estudiante-detail'),
]
