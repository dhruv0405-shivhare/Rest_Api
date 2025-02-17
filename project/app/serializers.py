from rest_framework import serializers
from .models import Student
class Stu_serializers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    stu_name=serializers.CharField(max_length=50)
    stu_email=serializers.EmailField()
    stu_contact=serializers.IntegerField()
    stu_address=serializers.CharField(max_length=50)

    def create(self, validated_data):

        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance