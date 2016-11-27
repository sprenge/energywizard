# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-27 17:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('household', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergieType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='e.g. Gas, Water', max_length=256, unique=True, verbose_name='energie type')),
                ('e_unit', models.CharField(help_text='e.g. KW', max_length=128, verbose_name='energy unit')),
            ],
            options={
                'verbose_name_plural': 'EnergieTypes',
            },
        ),
        migrations.CreateModel(
            name='MeterReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_reading', models.FloatField(verbose_name='meter reading')),
                ('ts', models.DateTimeField(verbose_name='timestamp measurement')),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household.Household')),
                ('meter_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='e.g. day counter elektricity', max_length=256, verbose_name='meter type')),
                ('variant', models.CharField(default='standard', max_length=256, verbose_name='variant')),
                ('color_whole', models.CharField(default='White digits on black blackground', max_length=128, verbose_name='color whole meter part')),
                ('max_whole', models.IntegerField(default=6, verbose_name='maximum number of figures whole meter part')),
                ('color_fraction', models.CharField(blank=True, default='White digits on black blackground', max_length=128, null=True, verbose_name='Color fraction figure')),
                ('max_fraction', models.IntegerField(default=4, verbose_name='maximum number of figures fraction part')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo meter (200x200)')),
                ('energie_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.EnergieType')),
            ],
        ),
        migrations.AddField(
            model_name='meterreading',
            name='meter_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.MeterType'),
        ),
        migrations.AlterUniqueTogether(
            name='meterreading',
            unique_together=set([('ts', 'household', 'meter_type')]),
        ),
    ]