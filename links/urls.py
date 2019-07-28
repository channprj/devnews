# django
from django.urls import path

# third-party
from rest_framework.routers import DefaultRouter

# app
from . import views


router = DefaultRouter()
router.register(r'', views.LinkViewSet, basename='link')

urlpatterns = [
] + router.urls
