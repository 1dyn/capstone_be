from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .models import User, Scholarship
from .serializer import UserSerializer, ScholarshipSerializer


# class UserPageNumberPagination(PageNumberPagination):
#     page_size = 30
#
# class ScholarshipPageNumberPagination(PageNumberPagination):
#     page_size = 30

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = UserPageNumberPagination

class ScholarshipViewSet(ModelViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    # pagination_class = ScholarshipPageNumberPagination