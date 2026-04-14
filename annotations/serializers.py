from rest_framework import serializers
from .models import Annotation

class AnnotationSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Annotation
        fields = ['id', 'image', 'label', 'x', 'y', 'width', 'height', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']