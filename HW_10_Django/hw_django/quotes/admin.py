from django.contrib import admin
from django.utils.html import format_html

from .models import Author, Tag, Quote


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "fullname", "born_date", "born_location", "description", "picture", "created_at"]
    list_filter = ["fullname"]
    ordering = ("fullname",)
    search_fields = ["fullname", "born_location"]

    def image_tag(self, obj):
        return format_html('<img src="{}" height="140">'.format(obj.picture))


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "quote", "display_tags", "author", "created_at"]
    list_filter = ['tags']
    # ordering = ('author',)
    search_fields = ['author__fullname', 'tags__name']

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    display_tags.short_description = "Tags"

    def image_tag(self, obj):
        return format_html('<img src="{}" height="45">'.format(obj.author.picture))


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']


admin.site.site_header = "Quotes Collection"
admin.site.site_title = "Quotes"
