from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Inquiry, Area
from django.contrib.auth.models import User
from .serializers import InquirySerializer, AreaSerializer, UserSerializer


# Create your views here.

class InquiryViewSet(ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
