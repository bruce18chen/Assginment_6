# In forms.py

from django import forms
from .models import ContestEntry
from .models import Comment

class ContestEntryForm(forms.ModelForm):
    class Meta:
        model = ContestEntry
        fields = ['first_name', 'last_name', 'email', 'image']

# forms.py


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

