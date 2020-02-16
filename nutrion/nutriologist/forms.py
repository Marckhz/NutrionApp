from django import forms
from .models import Patients


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput() )


class SearchBarForm(forms.Form):

    search_bar = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'Buscar Clientes'}))

class GoogleCalendarForm(forms.Form):

    title = forms.CharField()
    date_start = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))# widget=forms.TextInput(attrs={'type':'datetime', }))# 'class':'form-control'} ))
    date_end = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))#  widget=forms.TextInput(attrs={'type':'datetime'}) )#, 'class':'form-control'}))
    start_hour = forms.TimeField(widget=forms.TextInput(attrs={'type':'time'}))
    end_time = forms.TimeField(widget=forms.TextInput(attrs={'type':'time'}))
    patient = forms.ModelChoiceField(queryset=Patients.objects.all() )
    location = forms.CharField()
    description = forms.CharField()
