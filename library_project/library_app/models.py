from django.db import models

# Create your models here.
class user_details(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table='user_info'
class user_reg(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table='user_registration'