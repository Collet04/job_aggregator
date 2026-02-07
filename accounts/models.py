from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField( upload_to="profiles/",default="profiles/default.png")
    middle_name = models.CharField(max_length=50, blank=True)  # optional
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
