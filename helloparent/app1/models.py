from django.db import models

# Create your models here.
class Student(models.Model):
    Rollno=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    branch=models.CharField(max_length=100)
    dob = models.DateField()
    gender=models.CharField(max_length=20)
    Mentor=models.CharField(max_length=40)
    image=models.ImageField(upload_to='files/covers')

    def __str__(self):
        return f'Student:{self.name}'    
class academics(models.Model):
    rollno=models.CharField(max_length=20)
    LADC=models.PositiveIntegerField()
    AP=models.PositiveIntegerField()
    ENG=models.PositiveIntegerField()
    DM=models.PositiveIntegerField()
    VEGC=models.PositiveIntegerField()
    Java=models.PositiveIntegerField()
    DLD=models.PositiveIntegerField()
    BEE=models.PositiveIntegerField()
    DBMS=models.PositiveIntegerField()
    PS=models.PositiveIntegerField()
    CHEM=models.PositiveIntegerField()
    SLL=models.PositiveIntegerField()
    DBMSL=models.PositiveIntegerField()
    JPL=models.PositiveIntegerField()
    LSPD=models.PositiveIntegerField()
    DEVC=models.PositiveIntegerField()
    EWS=models.PositiveIntegerField()
    DS=models.PositiveIntegerField()
    DSL=models.PositiveIntegerField()
    def __str__(self):
        return f'Progress:{self.rollno}'


    

    

