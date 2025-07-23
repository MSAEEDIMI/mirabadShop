from django.db import models



class Otp(models.Model):
    token=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    code=models.CharField(max_length=4)
    expiration_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.phone