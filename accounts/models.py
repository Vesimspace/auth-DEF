from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    nick_name = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='account_photos/%Y/%m/')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Accounts'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo.path)
            if image.height > 600 or image.width > 600:
                output_size = (600, 600)
                image.thumbnail(output_size)
                image.save(self.photo.path)

    
class AccountStatus(models.Model):
    user_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status_message = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_account)
    
    class Meta:
        verbose_name_plural = 'Account Status'