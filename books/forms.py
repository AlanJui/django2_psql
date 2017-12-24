from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Author, Book, Publisher

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ('name', 'email', 'headshot')

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         labels = {
#             'name': _('Writer'),
#         }
#         help_texts = {
#             'name': _('Some useful help text.'),
#         }
#         error_messages = {
#             'name': {
#                 'max_length': _("This writer's name is too long."),
#             },
#         }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'authors',
            'publisher',
            'publication_date',
        ]

