from .models import Student
from .serializers import Stu_serializers
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = Stu_serializers
    