from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Log
from .serializers import LogSerializer

class LogListView(APIView):
    def get(self, request):
        logs = Log.objects.all().order_by('-timestamp')
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)