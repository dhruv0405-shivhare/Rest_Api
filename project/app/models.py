from django.db import models

class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_address=models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name
    

class Employee(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_address=models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name




class Cart(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_address=models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name




class Admin(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_address=models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name


class Cart1(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_address=models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name

