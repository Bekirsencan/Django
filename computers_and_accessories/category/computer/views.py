from rest_framework import generics
from .models import Computer
from .serializers import ComputerSerializer


class GetComputers(generics.ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
