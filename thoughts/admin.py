from django.contrib import admin
from .models import ThoughtsV1


@admin.register(ThoughtsV1)
class ThoughtsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'associated_to', 'DOP', 'duration', 'published_at']
    list_filter = ['associated_to', 'duration', 'published_at']
    search_fields = ['title', 'associated_to', 'published_at']