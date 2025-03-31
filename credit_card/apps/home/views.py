from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class HomeView(APIView):


    def get(self, request):
        return Response({"mensaje": "¡Bienvenido al Endpoint!"})
