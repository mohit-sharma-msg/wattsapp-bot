from django import forms
from .models import *
  
class pdfForm(forms.ModelForm):
  
    class Meta:
        model = whatsappdb
        fields = ['name', 'contact','pdf','photo']