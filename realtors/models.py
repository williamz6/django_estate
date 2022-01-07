from django.db import models
from datetime import datetime
from PIL import Image

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    
    # def save(self):
    #     super().save()
    #     img = Image.open(self.photo.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size= (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)

