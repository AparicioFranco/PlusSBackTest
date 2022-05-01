from rest_framework.serializers import ModelSerializer
from .models import Inquiry, Area
from django.contrib.auth.models import User


class InquirySerializer(ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id', 'description', 'area', 'owner']


class AreaSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
