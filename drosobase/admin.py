# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Stocks


class StocksAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                 {'fields': ['post_title', 'post_content']}),
        ('Date information',   {'fields': ['post_date'], 'classes': ['collapse']}),
        ]
    list_display = ('post_title', 'post_content', 'post_date')
    search_fields = ['post_title', 'post_content']

admin.site.register(Stocks, StocksAdmin)
