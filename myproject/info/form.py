from django import forms



class ContactForm(forms.Form):
    Source = forms.CharField()
    Destination = forms.CharField()
    email = forms.EmailField()
