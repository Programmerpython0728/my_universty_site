from django.db import models


class Faculty(models.Model):


    objects = None
    name=models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return f"{self.name}"

class Kafedra(models.Model):
    objects = None
    name=models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.name

class Subject(models.Model):
    objects = None
    name=models.CharField(max_length=200,blank=False,null=False)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    objects = None
    name=models.CharField(max_length=200,null=False,blank=False)
    last_name=models.CharField(max_length=200,null=False,blank=False)
    def __str__(self):
        return self.name,self.last_name

class Group(models.Model):
    objects = None
    name=models.CharField(max_length=200,null=False,blank=False)
    def __str__(self):
        return self.name
class Student(models.Model):
    objects = None
    name=models.CharField(max_length=200,null=False,blank=False)
    last_name=models.CharField(max_length=200,null=False,blank=False)
    def __str__(self):
        return self.name,self.last_name



