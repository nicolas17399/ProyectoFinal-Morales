from django import forms
from AppNerilan.models import *


class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    metododepago = forms.CharField()
    tienedeuda=forms.BooleanField()

class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField()
    antiguedad = forms.IntegerField()
    email=forms.EmailField()

class FinanzasFormulario(forms.Form):
    gastos = forms.IntegerField()
    ganancias = forms.IntegerField()