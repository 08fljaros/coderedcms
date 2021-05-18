# Generated by Django 3.1.7 on 2021-04-09 19:51

import coderedcms.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coderedcms', '0019_spelling_corrections'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyticssettings',
            name='body_scripts',
            field=coderedcms.fields.ScriptField(blank=True, help_text='Add tracking scripts toward closing <body> tag.', null=True, verbose_name='<body> tracking scripts'),
        ),
        migrations.AddField(
            model_name='analyticssettings',
            name='head_scripts',
            field=coderedcms.fields.ScriptField(blank=True, help_text='Add tracking scripts between the <head> tags.', null=True, verbose_name='<head> tracking scripts'),
        ),
    ]