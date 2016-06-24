from django import forms
from .models import Cliente
from django.forms import Form


class DisponibiliddadForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellidos', 'ciudad', 'direccion', 'codigo_postal', 'telefono', 'email', 'c_email', 'tyc',)

        widgets = {
            'nombre': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
            'c_email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
            'tyc': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }

