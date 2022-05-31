from rest_framework.serializers import ModelSerializer

from projects.models import Project
from projects.models import Tag

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag 
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('date_published',)
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}

