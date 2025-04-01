from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore


# Create your views here.
class HomeView(APIView):
    permission_classes = [IsAuthenticated]  # Se requiere autenticación

    def get(self, request):
        return Response({"mensaje": "¡Bienvenido al Endpoint!"})
