from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from projects.models import Project
from projects.models import Tag
from projects.serializers import ProjectSerializer
from projects.serializers import TagSerializer

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `list`, `retrieve`, `update`, and `destroy` actions.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'slug'

class TagViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `list`, `retrieve`, `update`, and `destroy` actions.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
