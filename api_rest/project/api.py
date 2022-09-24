# Django Rest Framework Imports.
from rest_framework import viewsets , permissions

# Local Imports.
from .models import Project
from .serializers import ProjectSerializer


# Project ViewSet.
class ProjectViewSet(viewsets.ModelViewSet):
    
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class= ProjectSerializer