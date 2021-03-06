from django import forms

from .models import Person

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here'
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'style': 'border-color: green;'
            }
        )
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                'style': 'border-color: orange;'
            }
        ),
        help_text='Write here your message!'
    )

    # name = forms.CharField(max_length=30)
    # email = forms.EmailField(max_length=254)
    # message = forms.CharField(
    #     max_length=2000,
    #     widget=forms.Textarea(),
    #     help_text='Write here your message!'
    # )
    """
    A hidden input for internal use
    tell from which page the user sent the message
    """
    source =forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone', 'bio',)
