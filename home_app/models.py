from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    title=models.CharField(max_length=50)
    phone=models.CharField(max_length=11)
    instagram=models.URLField(max_length=200,null=True)
    rubika=models.URLField(max_length=200,null=True)
    telegram=models.URLField(max_length=200,null=True)
    discreption=models.TextField()
    logo=models.ImageField(upload_to="logo")
    name1=models.CharField(max_length=50)
    perseneImage1=models.ImageField(upload_to="modiriat")
    name2=models.CharField(max_length=50)
    perseneImage2=models.ImageField(upload_to="modiriat")
    name3=models.CharField(max_length=50)
    perseneImage3=models.ImageField(upload_to="modiriat")
    def __str__(self):
        return f"titel of the site is ({self.title})"


class Banner(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True, null=True)
    position = models.CharField(max_length=50, choices=[
        ('main', 'بنر اصلی'),
        ('sidebar', 'سایدبار'),
        ('footer', 'بنر پایین صفحه'),
    ])
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position
