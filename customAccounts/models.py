from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("ایمیل باید وارد شود")
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('سوپریوزر باید is_staff=True باشد.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('سوپریوزر باید is_superuser=True باشد.')

        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,blank=True,null=True,verbose_name="ایمیل")
    phone=models.CharField(max_length=12,unique=True,verbose_name='شماره تلفن')
    first_name = models.CharField(max_length=30, blank=True,verbose_name='نام')
    last_name = models.CharField(max_length=30, blank=True,verbose_name='نام خانوادگی')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False,verbose_name='ادمین')
    date_joined = models.DateTimeField(default=timezone.now,verbose_name='لحضه عضویت')

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name+" " +self.last_name

        
    class Meta:
        verbose_name_plural="حساب های کاربری "
        verbose_name="حساب"