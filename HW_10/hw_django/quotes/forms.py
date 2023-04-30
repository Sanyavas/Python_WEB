from django.forms import ModelForm, CharField, TextInput, ModelMultipleChoiceField, ModelChoiceField, Select, \
    SelectMultiple, Textarea
from .models import Quote, Author, Tag


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, required=True,
                      widget=Textarea({'class': "form-control", 'id': "quote", "rows": "3"}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"), required=True,
                                    widget=SelectMultiple({'multiple class': "form-control", 'id': "tags"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by("fullname"),
                              widget=Select({'class': "form-control", 'id': "author"}))

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'fullname',
        'placeholder': 'fullname'}))
    born_date = CharField(max_length=50, widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'born_date',
        'placeholder': 'born date'}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'born_location',
        'placeholder': 'born location'}))
    description = CharField(widget=Textarea(attrs={
        'class': 'form-control',
        'id': 'description',
        'placeholder': 'description'}))
    picture = CharField(max_length=300, widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'picture',
        'placeholder': 'https://.....Aristotle_Altemps_Inv8575.jpg'}))

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description", "picture"]


class TagForm(ModelForm):
    name = CharField(max_length=50, widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'placeholder': 'name'}))

    class Meta:
        model = Tag
        fields = ["name"]
