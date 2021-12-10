from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django_filters.rest_framework import DjangoFilterBackend

from .models import Computer
from .serializers import ComputerSerializer
from .filters import ComputerFilter

from rest_framework.decorators import api_view


# class GetComputers(generics.ListAPIView):
#     queryset = Computer.objects.all()
#     serializer_class = ComputerSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_class = ComputerFilter

@api_view(['GET'])
@login_required()
def get_computer(request):
    queryset = Computer.objects.all()
    serializer = ComputerSerializer(queryset, many=True)
    return Response(serializer.data)


class GetComputers(APIView):

    @method_decorator(login_required)
    def get(self, request):
        print(request.user.username)
        queryset = Computer.objects.all()
        serializer = ComputerSerializer(queryset, many=True)
        return Response(serializer.data)
