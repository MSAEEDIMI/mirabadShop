from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    title=models.CharField(max_length=50,verbose_name='عنوان سایت')
    phone=models.CharField(max_length=11,verbose_name='شماره پشتیبانی')
    instagram=models.URLField(max_length=200,null=True,verbose_name='ایدی اینستاگرام')
    rubika=models.URLField(max_length=200,null=True,verbose_name='ایدی روبیکا')
    telegram=models.URLField(max_length=200,null=True,verbose_name='ایدی تلگرام')
    discreption=models.TextField(verbose_name='توضیحات سایت')
    logo=models.ImageField(upload_to="logo",verbose_name='لگوی سایت')
    name1=models.CharField(max_length=50,verbose_name='نام پرسنل ۱')
    perseneImage1=models.ImageField(upload_to="modiriat",verbose_name='عکس پرسنل ۱')
    name2=models.CharField(max_length=50,verbose_name='نام پرسنل۲')
    perseneImage2=models.ImageField(upload_to="modiriat",verbose_name='عکس پرسنل۲')
    name3=models.CharField(max_length=50,verbose_name='نام پرسنل۳')
    perseneImage3=models.ImageField(upload_to="modiriat",verbose_name='عکس پرسنل۳')
    def __str__(self):
        return f"titel of the site is ({self.title})"
    class Meta:
        verbose_name=' اطلاعات سایت و پرسنل'
        verbose_name_plural=' اطلاعات سایت و پرسنل'

class Banner(models.Model):
    title = models.CharField(max_length=200, blank=True,verbose_name='عنوان')
    image = models.ImageField(upload_to='banners/',verbose_name='عکس')
    link = models.URLField(blank=True, null=True,verbose_name='لینک ')
    position = models.CharField(max_length=50, choices=[
        ('main', 'اسلایدر اصلی'),
        ('sidebar', 'بنر کنار اسلایدر'),
        ('footer', 'بنر پایین صفحه'),
    ],verbose_name='جایگاه')
    order = models.PositiveIntegerField(default=0,verbose_name='اولویت نمایش')

    def __str__(self):
        return self.position
    class Meta:
        verbose_name=' اسلایدر و بنرها'
        verbose_name_plural='اسلایدر و بنر '