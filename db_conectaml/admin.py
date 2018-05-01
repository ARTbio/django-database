
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Patients, Sequencing


class SequencingInline(admin.StackedInline):
    model = Sequencing
    extra = 1

class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                 {'fields': ['name', 'sex', 'age']}),
        ('Date information',   {'fields': ['date_diagnosis'], 'classes': ['collapse']}),
        ]
    inlines = [SequencingInline]
    list_display = ('name', 'age', 'date_diagnosis', 'was_diagnosed_recently')
    list_filter = ['date_diagnosis']
    search_fields = ['name']

admin.site.register(Patients, PatientAdmin)
# admin.site.register(Sequencing)
