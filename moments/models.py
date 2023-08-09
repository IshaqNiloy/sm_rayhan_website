from django.db import models

# Create your models here.


class Moment(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    associated_to = models.CharField(max_length=250)
    image = models.FileField()
    alternate_text = models.CharField(max_length=250)
    header = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'moment'
        verbose_name_plural = 'moments'

    def __str__(self):
        return self.description