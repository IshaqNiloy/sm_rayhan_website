from django.db import models
from django_resized import ResizedImageField
# Create your models here.


class Moment(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    associated_to = models.CharField(max_length=250)
    image = ResizedImageField(size=[500, 300], null=False, blank=False)
    alternate_text = models.CharField(max_length=250)
    header = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'moment'
        verbose_name_plural = 'moments'

    def __str__(self):
        return self.description


class EmbeddedMoment(models.Model):
    moment = models.ForeignKey(Moment, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True, editable=False)
    associated_to = models.CharField(max_length=250)
    image = ResizedImageField(size=[500, 300], null=False, blank=False)
    alternate_text = models.CharField(max_length=250)
    header = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'embedded moment'
        verbose_name_plural = 'embedded moments'

    def __str__(self):
        return self.description

