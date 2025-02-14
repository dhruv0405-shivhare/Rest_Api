from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import Stu_serializers
def stu_list(request):
    stu=Student.objects.all()
    print(stu)
    serializer = Stu_serializers(stu,many=True)
    print(serializer)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)

def stu_details(request):
    pass
