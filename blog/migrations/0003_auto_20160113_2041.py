# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_left',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_right',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right', to='blog.Post'),
        ),
    ]
