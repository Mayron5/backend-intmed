from django.contrib.auth.models import AbstractUser

class Cliente(AbstractUser):
    def __str__(self):
        return self.email
