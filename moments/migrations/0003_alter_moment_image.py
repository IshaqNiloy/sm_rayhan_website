# Generated by Django 4.2.3 on 2023-09-02 13:45

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('moments', '0002_embeddedmoment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 300], upload_to=''),
        ),
    ]
