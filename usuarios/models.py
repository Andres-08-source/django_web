from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = [
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('fullstack', 'Fullstack'),
]

class Usuario(AbstractUser):
    rol = models.CharField(max_length=10, choices=ROLES, default='fullstack')

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
