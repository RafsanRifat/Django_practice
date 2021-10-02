from django import forms
from .models import Contact


class ContactForm(forms.Form):
    # class Meta:
    #     model = Contact
    #     fields = '__all__'
    name = forms.CharField(max_length=100, label='Your Name:')
    email = forms.CharField(max_length=18, label='Your Phone Number')
    text = forms.CharField(max_length=500, label='About You:')
