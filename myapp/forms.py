from django import forms
from .models import Contact, Post

"""
=======>>> Django form : 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name:')
    email = forms.CharField(max_length=18, label='Your Phone Number')
    text = forms.CharField(max_length=500, label='About You:')
    
"""


# ========>>> Django model form:

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'id', 'created_at', 'slug', ]
        widgets = {  # This is using for checkboxselectmultiple
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple': True
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True
            })
        }
