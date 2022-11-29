from django.db import models

# Create your models here.
class travelinfo(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

    # def __str__(self):
    #     return self.name
class team_info(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
    about=models.TextField()
