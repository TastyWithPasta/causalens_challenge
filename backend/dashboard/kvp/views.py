from django.shortcuts import render

# Create your views here.
from .models import Kvp
from .serializers import KvpSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class KvpViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Kvp.objects.all()
    serializer_class = KvpSerializer