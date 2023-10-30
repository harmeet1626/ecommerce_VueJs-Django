from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=25)
    dob = models.DateField()
    image = models.CharField(max_length=500, default=0)
    is_seller = models.BooleanField(default=False)
    class Meta:
	    db_table = "User"
    

