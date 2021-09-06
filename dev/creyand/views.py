from django.shortcuts import render
from .models import ADMIN_REQ
from rest_framework import viewsets
from .serializers import ADMIN_REQ_seializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView

# Create your views here.
class ADMIN_REQ(viewsets.ModelViewSet):
    queryset = ADMIN_REQ.objects.all()
    serializer_class = ADMIN_REQ_seializers