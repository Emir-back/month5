from django.contrib.auth.models import AbstractUser 
from django.conf import settings
from django.db import models
import random

class CustomUser(AbstractUser):
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def generate_code(self):
        code = str(random.randint(100000, 999999))
        self.confirmation_code = code
        self.save()
        return code
    
class ConfirmationCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

