from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


class Otp(models.Model):
    token=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    code=models.CharField(max_length=4)
    expiration_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.phone
    
    
class AddressModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='addresses',verbose_name='کاربر')
    full_name=models.CharField(verbose_name='نام تحویل گیرنده')
    phone=models.CharField(max_length=12,verbose_name="شماره تلفن تحویل گیرنده")
    address=models.TextField(max_length=300,verbose_name='آدرس')
    postal_code=models.CharField(max_length=16,verbose_name='کد پستی')
    
    def __str__(self):
        if self.user.first_name or self.user.last_name:
            return self.user.first_name+" " +self.user.last_name
        else:
            return self.user.phone     # type: ignore

        
    class Meta:
        verbose_name_plural="آدرس ها  "
        verbose_name="آدرس"
        
   