# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-26 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.IntegerField(choices=[(1, 'No paga'), (2, 'Paga'), (3, 'Anulada/Cancelada'), (4, 'Abono')], default=1),
        ),
    ]
