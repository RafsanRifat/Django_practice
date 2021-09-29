from django import forms
from  .models import Contact


class ContactForm(forms.ModelForm):
    # class Meta:
    #     model = Contact
    #     fields = '__all__'
    name = forms.CharField(max_length=100, label='Your Name:')
    number = forms.CharField(max_length=18, label='Your Phone Number')
    text = forms.CharField(max_length=500, label='About You:')
