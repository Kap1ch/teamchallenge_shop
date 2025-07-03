from django.db import models
from django.utils.text import slugify

from apps.core.models import BaseModel


class Catalog(BaseModel):
    name = models.CharField(max_length=80, verbose_name='Catalog name')
    image_url = models.ImageField(upload_to='category_image/')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Catalog, self).save(*args, **kwargs)


class SubCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.ImageField(upload_to='subcategory_image/')
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(SubCategory, self).save(*args, **kwargs)
