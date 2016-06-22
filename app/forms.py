__author__ = 'seader'
from django import  forms


class DisponibiliddadForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput( attrs={ 'type':'date', 'class': 'form-control'}))