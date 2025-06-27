from django.db import models

from apps.core.models import BaseModel


# Create your models here.

class Catalog(BaseModel):
    name = models.CharField(max_length=80, verbose_name='Catalog name')
    img = models.ImageField(upload_to='category_image/')

    def __str__(self):
        return str(self.name)



class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return str(self.name)