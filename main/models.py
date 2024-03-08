from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image=models.ImageField(blank=True,upload_to='posts_images')
    def imageurl(self):
        try:
            return self.image.url
        except:
            img=''
            return img


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField( default='default.png', upload_to='images')

    def save(self):
        super().save()
        img=Image.open(self.user.profile.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.user.profile.image.path)  


