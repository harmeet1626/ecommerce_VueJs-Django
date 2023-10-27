from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add your custom fields here
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField()
    dob = models.DateField()
    image = models.CharField(max_length=50, default=0)
    class Meta:
	    db_table = "User"
    

