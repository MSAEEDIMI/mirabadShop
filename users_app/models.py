from django.db import models



class Otp(models.Model):
    phone=models.CharField(max_length=12)
    code=models.CharField(max_length=4)
    