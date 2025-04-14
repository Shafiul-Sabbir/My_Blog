from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from cloudinary.models import CloudinaryField
import requests
from io import BytesIO

# # Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    image = CloudinaryField('image', blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and self.image.url:
            response = requests.get(self.image.url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    # No need to re-upload or resave here, because Cloudinary already handles resizing with transformations

    # # image optimization
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     if self.image and self.image != 'default.jpg':
    #         img = Image.open(self.image)
    #         if img.height > 300 or img.width > 300:
    #             output_size = (300, 300)
    #             img.thumbnail(output_size)
    #             in_mem_file = ContentFile(img.tobytes())
    #             img.save(in_mem_file, img.format)
    #             in_mem_file.seek(0)
    #             self.image.save(self.image.name, in_mem_file, save=False)  # Save to the same file
    #             super().save(*args, **kwargs)