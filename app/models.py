from django.db import models

# Create your models here.

# Departartment table

class Dept(models.Model):
  deptNo = models.IntegerField(primary_key=True)
  dname = models.CharField(max_length=50,null=False)
  loc = models.CharField(max_length=30,null=False)

# Employee table 

class Emp(models.Model):
  empNo = models.IntegerField(primary_key=True)
  ename = models.CharField(max_length=50,null=False)
  job = models.CharField(max_length=30, null=False)
  mgr = models.IntegerField()
  sal = models.IntegerField()
  
# Bonus table

class Bonus(models.Model):
  ename = models.CharField(max_length=50,primary_key=True)
  job=models.CharField(max_length=30, null=False)
  sal= models.IntegerField()
  comm=models.IntegerField()

# Salgrade table 

class SalGrade(models.Model):
  grade=models.IntegerField()
  losal=models.IntegerField()
  hisal=models.IntegerField()
  