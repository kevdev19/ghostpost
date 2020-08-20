from django import forms
from ghostpostapp.models import RoastBoastModel


class NewPostForm(forms.Form):
    CHOICES = [(True, 'boast'), (False, 'roast')]
    is_boast = forms.ChoiceField(choices=CHOICES)
    content = forms.CharField(widget=forms.TextInput(), max_length=280)
