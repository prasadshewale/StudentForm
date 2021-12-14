
from django.db import models

# Create your models here.
class Contact(models.Model):
    stud_email=models.EmailField(max_length=100, primary_key=True)
    par_email=models.EmailField(max_length=100)
    stud_first_name=models.CharField(max_length=100)
    stud_last_name=models.CharField(max_length=100)
    par_first_name=models.CharField(max_length=100)
    par_last_name=models.CharField(max_length=100)
    stud_address=models.CharField(max_length=100)
    par_address=models.CharField(max_length=100)
    stud_phone=models.CharField(max_length=100)
    par_phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)   
    occupation=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    category=models.CharField(max_length=100)
    SSC_marks=models.CharField(max_length=100)
    HSC_marks=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.stud_first_name} {self.stud_last_name}'