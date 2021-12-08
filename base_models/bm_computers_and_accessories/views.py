from django.shortcuts import render
from .models import BaseModelComputerAndAccessories
from rest_framework import generics


class Show(generics.ListAPIView):
    queryset = BaseModelComputerAndAccessories.objects.all()

