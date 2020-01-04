from django.db import models

# Create your models here.
class Customers(models.Model):

    def __str__(self):
        return self.name+'_'+str(self.money)

    name= models.CharField(max_length=100)
    money=models.IntegerField()

