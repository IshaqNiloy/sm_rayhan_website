from django.db import models
from django.utils import timezone
from .manager import ThoughtsManager


class ThoughtsV1(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=250, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    associated_to = models.CharField(max_length=250, null=True, blank=True)
    DOP = models.DateField(null=False, blank=False)
    duration = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=250)
    image = models.FileField(null=False, blank=False)
    alternate_text_for_image = models.CharField(max_length=250, null=True, blank=True)
    article = models.TextField(null=False, blank=False)
    youtube_video_url = models.CharField(max_length=250, null=True, blank=True)
    published_at = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    objects = ThoughtsManager()

    class Meta:
        verbose_name = 'Thought'
        verbose_name_plural = 'Thoughts'

    def __str__(self):
        return self.title

