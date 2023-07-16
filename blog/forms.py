# In forms.py

from django import forms
from .models import ContestEntry

class ContestEntryForm(forms.ModelForm):
    class Meta:
        model = ContestEntry
        fields = ['first_name', 'last_name', 'email', 'image']

