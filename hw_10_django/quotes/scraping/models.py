from bson import json_util
from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE
from django.conf import settings


connect(db=settings.MONGO_DB, host=settings.MONGO_URI)


class Author(Document):
    fullname = StringField(required=True, max_length=50, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField(max_length=4000)
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=200))
    quote = StringField(max_length=4000)
    meta = {"collection": "quotes"}

    def to_json(self, *args, **kwargs):
        data = self.to_mongo(*args, **kwargs)
        data["author"] = self.author.fullname
        return json_util.dumps(data, ensure_ascii=False)
