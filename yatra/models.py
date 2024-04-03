from django.db import models

# Create your models here.
class PersonalP(models.Model):

    name = models.CharField(max_length = 30)
    Address = models.CharField(max_length = 30)
    Phone =models.IntegerField()
    Mobile = models.IntegerField()
    E_mail = models.EmailField()
    Aadhar_card = models.IntegerField()


