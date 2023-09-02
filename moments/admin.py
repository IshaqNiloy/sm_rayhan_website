from django.contrib import admin
from .models import Moment, EmbeddedMoment
# Register your models here.


@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ['id', 'associated_to', 'image', 'alternate_text', 'header', 'description']
    list_filter = ['associated_to']
    search_fields = ['associated_to']


@admin.register(EmbeddedMoment)
class EmbeddedMomentAdmin(admin.ModelAdmin):
    list_display = ['id', 'associated_to', 'image', 'alternate_text', 'header', 'description']
    list_filter = ['associated_to']
    search_fields = ['associated_to']

