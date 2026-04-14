from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
from logs.models import Log

class ImageListView(APIView):
    def get(self, request):
        images = Image.objects.all().order_by('-created_at')
        serializer = ImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            image = serializer.save(uploaded_by=request.user)
            Log.objects.create(user=request.user, activity=f"Upload gambar ID {image.id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetailView(APIView):
    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return None

    def get(self, request, pk):
        image = self.get_object(pk)
        if not image:
            return Response({'error': 'Gambar tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ImageSerializer(image, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, pk):
        image = self.get_object(pk)
        if not image:
            return Response({'error': 'Gambar tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
        Log.objects.create(user=request.user, activity=f"Hapus gambar ID {pk}")
        image.delete()
        return Response({'message': 'Gambar berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)