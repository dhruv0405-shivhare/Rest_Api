from .models import Student
from .serializers import Stu_serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class Stu_List(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Stu_serializers


class Stu_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Stu_serializers