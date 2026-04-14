from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Annotation
from .serializers import AnnotationSerializer
from images.models import Image
from logs.models import Log

class AnnotationListView(APIView):
    def get(self, request, image_id):
        annotations = Annotation.objects.filter(image_id=image_id)
        serializer = AnnotationSerializer(annotations, many=True)
        return Response(serializer.data)

    def post(self, request, image_id):
        try:
            image = Image.objects.get(pk=image_id)
        except Image.DoesNotExist:
            return Response({'error': 'Gambar tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnnotationSerializer(data=request.data)
        if serializer.is_valid():
            annotation = serializer.save(image=image, created_by=request.user)
            Log.objects.create(user=request.user, activity=f"Tambah anotasi '{annotation.label}' pada gambar ID {image_id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnnotationDetailView(APIView):
    def get_object(self, pk):
        try:
            return Annotation.objects.get(pk=pk)
        except Annotation.DoesNotExist:
            return None

    def put(self, request, pk):
        annotation = self.get_object(pk)
        if not annotation:
            return Response({'error': 'Anotasi tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnnotationSerializer(annotation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            Log.objects.create(user=request.user, activity=f"Edit anotasi ID {pk}")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        annotation = self.get_object(pk)
        if not annotation:
            return Response({'error': 'Anotasi tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        Log.objects.create(user=request.user, activity=f"Hapus anotasi ID {pk}")
        annotation.delete()
        return Response({'message': 'Anotasi berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)