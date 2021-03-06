# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import (Category, Topic, Entry, Favoutire)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('user', 'title',)
    search_fields = ('title',)
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
    )
    filter_horizontal = ('category',)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Favoutire)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user',)
