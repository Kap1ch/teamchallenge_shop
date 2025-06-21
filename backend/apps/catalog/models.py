from django.db import models

from apps.core.models import BaseModel


# Create your models here.

class Catalog(BaseModel):
    name = models.CharField(max_length=80, verbose_name='Catalog name')
    img = models.ImageField(upload_to='category_image/')

    def __str__(self):
        return str(self.name)