# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from dictionary.users.models import User
from .signals import check_junior


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name=_("Title")
    )
    class Meta:
        verbose_name_plural = _("Kategoriler")

    def __str__(self):
        return "#{title}".format(title=self.title)


@python_2_unicode_compatible
class Topic(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=140,
        unique=True,
        verbose_name=_("Title")
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Created at")
    )
    category = models.ManyToManyField(
        Category,
        blank=True,
        verbose_name=_("Category")
    )

    class Meta:
        verbose_name = _("Baslik")
        verbose_name_plural = _("Basliklar")
        ordering = ('created_at',)
    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Entry(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True
    )
    topic = models.ForeignKey(
        Topic,
        null=True,
        blank=True
    )
    content = models.TextField(
        verbose_name=_("Content")
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Created at")
    )
    class Meta:
        verbose_name_plural = _("Yorumlar")

    def __str__(self):
        return self.content

signals.post_save.connect(check_junior, sender=Entry)


@python_2_unicode_compatible
class Favoutire(models.Model):
    entry = models.ForeignKey(
        Entry,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = (('entry', 'user'),)
        verbose_name_plural = _("Favoriler")

    def __str__(self):
        return self.user.username

