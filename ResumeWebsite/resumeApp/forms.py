from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, max_length=64)
    contact_email = forms.EmailField(required=True, max_length=64)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
