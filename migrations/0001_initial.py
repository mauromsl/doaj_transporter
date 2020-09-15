# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-15 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('submission', '0048_submissionconfiguration_submission_file_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='DOAJArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doaj_id', models.CharField(max_length=255)),
                ('exported', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='submission.Article')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='doajarticle',
            unique_together=set([('article', 'doaj_id')]),
        ),
    ]
