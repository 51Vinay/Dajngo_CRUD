from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.id)+""+ self.name
    