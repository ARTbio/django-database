# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_conectaml', '0002_patients_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequencing',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_conectaml.Patients'),
        ),
    ]