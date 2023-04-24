from django.forms import ModelForm, CharField, TextInput
from .models import Quote, Author, Tag


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, required=True, widget=TextInput())
    tags = CharField(min_length=5, required=True, widget=TextInput())
    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['name', 'description']
        exclude = ['tags']