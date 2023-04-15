from django import forms
from AppNerilan.models import *
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    metododepago = forms.CharField()
    tienedeuda=forms.BooleanField()

class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField()
    antiguedadMeses = forms.IntegerField()
    email=forms.EmailField()
    recibo=forms.FileField()

class FinanzasFormulario(forms.Form):
    gastos = forms.IntegerField()
    ganancias = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()
    USER_CHOICES = (
        ('client', 'Client'),
        ('employee', 'Employee'),
    )
    user_type = forms.ChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name','user_type']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username=forms.ModelChoiceField(queryset=User.objects.all())
    imagen=forms.ImageField(required=True) 
    
    class Meta:
        model=User
        fields=['imagen']
        help_texts={k:"" for k in fields}