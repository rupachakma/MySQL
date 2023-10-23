from django.db import models

# Create your models here.
class Stu(models.Model):
    name=models.CharField(max_length=20)
    dob=models.DateField()

    class Meta:
        db_table="Stu"
    def __str__(self):
        return self.name
    
class people(models.Model):
    age=models.IntegerField()
    height=models.FloatField()
    student=models.OneToOneField(Stu,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table='people'