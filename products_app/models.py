
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=30)
    all_discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


UNIT_CHOICES = [
    ('kg', 'Kilogram'),   # کیلویی
    ('pack', 'Pack'),     # بسته‌ای
    ('pcs', 'Piece'),     # عددی (اگه نیاز شد)
]

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    name_to_english = models.CharField(max_length=50)
    base_price = models.IntegerField(help_text="قیمت پایه بدون تخفیف")

    discount = models.IntegerField(default=0, help_text="درصد تخفیف محصول")
    image = models.ImageField(upload_to="products_image", blank=True, null=True)
    
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='kg')
    unit_amount = models.DecimalField(max_digits=5, decimal_places=2, default=1, help_text="مقدار واحد (مثلاً 0.5 برای بسته نیم کیلو)") # type: ignore

    stock_quantity = models.DecimalField(max_digits=10, decimal_places=3, default=0, help_text="موجودی انبار") # type: ignore
    sales_count = models.PositiveIntegerField(default=0, help_text="تعداد فروش")

    likes = models.PositiveIntegerField(default=0, help_text="حداکثر 30 لایک")
    selected = models.BooleanField(default=True)
    
    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_to_english)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products_app:product", kwargs={"slug": self.slug})

    def sale(self, amount=1):
        self.sales_count += amount
        self.stock_quantity -= amount
        if self.stock_quantity < 0:
            self.stock_quantity = 0
        self.save()

    def add_like(self):
        self.likes = min(self.likes + 1, 30)
        self.save()
        return self.likes

    def final_price(self):
        discount_value = self.discount or self.category.all_discount or 0
        return round(self.base_price * (1 - discount_value / 100))

    def star_rating(self):
        max_likes = 30
        stars = (self.likes / max_likes) * 5
        return round(max(0, min(5, stars)), 1)

    def __str__(self):
        return self.name
