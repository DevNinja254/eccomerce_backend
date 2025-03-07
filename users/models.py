from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")   
    full_name = models.CharField(max_length=200)
    phone_number = models.IntegerField( null=True)
    country = models.CharField(max_length=200, default="kenya")
    county= models.CharField(max_length=200, default="mombasa")
    city = models.CharField(max_length=200, default="Mombasa")
    account_balance= models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to="profile_pics", default="default.jpg")

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)


