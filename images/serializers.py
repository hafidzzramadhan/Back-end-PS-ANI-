from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField()

    class Meta:
        model = Image
        fields = ['id', 'file', 'uploaded_by', 'created_at']
        read_only_fields = ['uploaded_by', 'created_at']