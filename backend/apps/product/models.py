from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from django.core.validators import MinValueValidator, MaxValueValidator

from apps.core.models import BaseModel
from apps.catalog.models import SubCategory


class Color(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Color name')
    color = ColorField(default='#FF000', verbose_name='Color in hex format')

    def __str__(self):
        return str(self.name)



class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Product name')
    description = models.TextField(verbose_name="Description product")
    material = models.CharField(max_length=255)
    depth = models.IntegerField(verbose_name='depth product')
    width = models.IntegerField(verbose_name='width product')
    height = models.IntegerField(verbose_name='height product')
    slug = models.SlugField(unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return str(self.name)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)


class Review(BaseModel):
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(verbose_name="Review")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.user} - review'


class ProductColor(BaseModel):
    image_url = models.ImageField(upload_to='product_image/')
    is_main = models.BooleanField(default=False, verbose_name='Main product image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productcolors')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='productcolors')

    def __str__(self):
        return f'{self.product.name} - {self.color.name} - main {self.is_main}'
