from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=100,blank=False, null=False)
    email=models.EmailField(blank=False, null=False)
    phone=models.CharField(max_length=15,blank=False, null=False)
    subject=models.CharField(max_length=200,blank=False, null=False)
    message=models.CharField(max_length=1000,blank=False, null=False)

    def __str__(self):
        return self.name
    

class booking(models.Model):
    name=models.CharField(max_length=100,blank=False, null=False)
    email=models.EmailField(blank=False, null=False)
    phone=models.CharField(max_length=15,blank=False, null=False)
    date=models.DateTimeField(null=False)
    disease=models.CharField(max_length=50,blank=False, null=False)

    def __str__(self):
        return self.name
    


