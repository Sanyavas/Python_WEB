from bson import ObjectId
from django import template

from ..utils import get_mongodb
# from ...utils.main_scrapy import run_scrapy

register = template.Library()


def get_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']


register.filter('author', get_author)
# register.filter('run_scrapy', run_scrapy)
