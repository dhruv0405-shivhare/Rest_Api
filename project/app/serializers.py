from rest_framework import serializers
from .models import Student

class Stu_serializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','stu_name','stu_email','stu_contact','stu_address']