# Generated by Django 4.2.3 on 2023-09-02 20:38

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('moments', '0003_alter_moment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embeddedmoment',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 300], upload_to=''),
        ),
    ]
