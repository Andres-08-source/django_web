from django import forms #type:ignore
from django.contrib.auth.forms import UserCreationForm #type:ignore
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rol = forms.ChoiceField(choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
    ])

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'password1', 'password2']
