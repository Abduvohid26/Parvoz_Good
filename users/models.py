from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics', default='default_profile_pic.jpeg')


    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)
        
    def save(self, *args, **kwargs):
        self.check_hash_password()
        super().save(*args, **kwargs)
