from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inquiry import views

router = DefaultRouter()
router.register('area', views.AreaViewSet, 'area')
router.register('inquiry', views.InquiryViewSet, 'inquiry')
router.register('user', views.UserViewSet, 'user')


urlpatterns = [
    path('', include(router.urls)),
]
