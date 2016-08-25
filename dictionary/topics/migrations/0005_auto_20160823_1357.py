# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-23 13:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_auto_20160822_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Yorumlar'},
        ),
        migrations.AlterModelOptions(
            name='favoutire',
            options={'verbose_name_plural': 'Favoriler'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topics.Topic'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favoutire',
            name='entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topics.Entry'),
        ),
        migrations.AlterField(
            model_name='favoutire',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]