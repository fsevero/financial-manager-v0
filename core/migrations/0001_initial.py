# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 16:46
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Saldo Inicial')),
                ('balance_date', models.DateField(default=datetime.date(2016, 3, 27), verbose_name='Data do saldo inicial')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'conta',
                'verbose_name_plural': 'contas',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'itens',
            },
        ),
        migrations.CreateModel(
            name='Montly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('signal', models.CharField(choices=[('R', 'Receita'), ('D', 'Despesa')], max_length=1, verbose_name='Sinal')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Account', verbose_name='Conta')),
            ],
            options={
                'verbose_name': 'mensal',
                'verbose_name_plural': 'mensais',
            },
        ),
        migrations.CreateModel(
            name='Payable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel', models.IntegerField(default=1, verbose_name='Parcela')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Valor')),
                ('date', models.DateField(verbose_name='Data')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('tags', models.CharField(blank=True, max_length=250, verbose_name='Tags')),
                ('paid', models.BooleanField(default=False, verbose_name='Pago?')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Account', verbose_name='Conta')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item', verbose_name='Item')),
            ],
            options={
                'verbose_name': 'despesa',
                'verbose_name_plural': 'despesas',
            },
        ),
        migrations.CreateModel(
            name='Receivable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel', models.IntegerField(default=1, verbose_name='Parcela')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Valor')),
                ('date', models.DateField(verbose_name='Data')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('tags', models.CharField(blank=True, max_length=250, verbose_name='Tags')),
                ('received', models.BooleanField(default=False, verbose_name='Recebido?')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Account', verbose_name='Conta')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item', verbose_name='Item')),
            ],
            options={
                'verbose_name': 'receita',
                'verbose_name_plural': 'receitas',
            },
        ),
    ]
