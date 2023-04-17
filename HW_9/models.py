from mongoengine import Document, StringField, ReferenceField, ListField, connect

connect(host="mongodb://localhost:27017/hw8")


class Author(Document):
    name = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()


class Quote(Document):
    author = ReferenceField(Author)
    tags = ListField(StringField(max_length=150))
    quote = StringField()
    meta = {'allow_inheritance': True}


class TextQuote(Quote):
    content = StringField()


class ImageQuote(Quote):
    image_path = StringField()


class LinkQueue(Quote):
    link_url = StringField()