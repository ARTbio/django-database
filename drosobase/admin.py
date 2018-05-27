# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Stocks, Flybase


class StocksAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                 {'fields': ['post_title', 'post_content']}),
        ('Date information',   {'fields': ['post_date'], 'classes': ['collapse']}),
        ]
    list_display = ('post_title', 'post_content', 'post_date')
    search_fields = ['post_title', 'post_content']


class FlybaseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['FBst_idx',
                            'collection_name',
                            'stock_type_cv',
                            'species',
                            'FB_genotype',
                            'description',
                            'stock_number']
                }),
        ]
    list_display = ('FBst_idx', 'FB_genotype', 'description')
    search_fields = ['FBst_idx', 'FB_genotype', 'description']

admin.site.register(Stocks,StocksAdmin)
admin.site.register(Flybase, FlybaseAdmin)
