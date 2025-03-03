from .models import Student
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = Stu_serializers

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Employee.objects.all()
    serializer_class = Employee_serializers

class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Cart.objects.all()
    serializer_class = Cart_serializers


class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Admin.objects.all()
    serializer_class = Admin_serializers


class Cart1ViewSet(viewsets.ModelViewSet):
    
    queryset = Cart1.objects.all()
    serializer_class = Cart1_serializers
    