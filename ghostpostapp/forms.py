from django import forms
from ghostpostapp.models import RoastBoastModel


class NewPostForm(forms.Form):
    CHOICES = [(True, 'boast'), (False, 'roast')]
    body = forms.Charfield(widget=forms.TextInput, max_length=280)
    is_boast = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
