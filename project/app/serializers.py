from rest_framework import serializers
from .models import Student
from .models import Employee
from .models import Cart
from .models import Admin
from .models import Cart1

class Stu_serializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class Employee_serializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class Cart_serializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class Admin_serializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

class Cart1_serializers(serializers.ModelSerializer):
    class Meta:
        model = Cart1
        fields = "__all__"                                