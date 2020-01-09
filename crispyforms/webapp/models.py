from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=130)
    Email=models.EmailField(blank=True)
    Job_Title=models.CharField(max_length=30,blank=True)
    BioData=models.TextField(blank=True)


