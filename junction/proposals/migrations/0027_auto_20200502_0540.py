# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-05-02 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proposals", "0026_auto_20200323_2010"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalproposal",
            name="video_url",
            field=models.URLField(
                blank=True,
                default="",
                help_text="A short 1-2 mins video link about your talk",
            ),
        ),
        migrations.AddField(
            model_name="proposal",
            name="video_url",
            field=models.URLField(
                blank=True,
                default="",
                help_text="A short 1-2 mins video link about your talk",
            ),
        ),
    ]