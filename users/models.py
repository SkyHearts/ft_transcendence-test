from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.user.username, filename)

# def user_directory_path1(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to=user_directory_path)
    isOnline = models.BooleanField(default=False)
    # friend_list = models.FilePathField(path=User.get_username() + 'flist.txt')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displ

@receiver(post_save, sender=User)
def init_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # print(user, sender, request)
    Profile.objects.all().filter(user=user).update(isOnline=True)

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    Profile.objects.all().filter(user=user).update(isOnline=False)