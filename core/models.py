# -*- coding: utf-8 -*-
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import date

class Account(models.Model):
  description = models.CharField(max_length=250)
  balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=u"Saldo Inicial")
  balance_date = models.DateField(verbose_name=u"Data do saldo inicial", default=date.today)
  user = models.ForeignKey(User, verbose_name="Usuário")

  def income(self):
    montly = self.montly_set.filter(signal='R')
    if montly.count() == 0:
      return Decimal(0.0)
    else:
      return Decimal(montly.aggregate(sum_value=models.Sum('value')).get('sum_value'))
  income.short_description = "Receitas"

  def expenses(self):
    montly = self.montly_set.filter(signal='D')
    if montly.count() == 0:
      return Decimal(0.0)
    else:
      return Decimal(montly.aggregate(sum_value=models.Sum('value')).get('sum_value'))
  expenses.short_description = "Despesas"

  def disponible(self):
    return self.income() - self.expenses()
  disponible.short_description = "Disponível"

  def pending_cpa(self):
    pending = self.payable_set.filter(paid=False)
    if pending.count() == 0:
      return Decimal(0.0)
    else:
      return Decimal(pending.aggregate(sum_value=models.Sum('value')).get('sum_value'))
  pending_cpa.short_description = "Pendente (Pagar)"

  def pending_cre(self):
    pending = self.receivable_set.filter(received=False)
    if pending.count() == 0:
      return Decimal(0.0)
    else:
      return Decimal(pending.aggregate(sum_value=models.Sum('value')).get('sum_value'))
  pending_cre.short_description = "Pendente (Receber)"

  def actual_balance(self):
    balance = self.balance

    pending = self.payable_set.filter(paid=True, date__gte=self.balance_date)
    if pending.count() > 0:
      balance -= Decimal(pending.aggregate(sum_value=models.Sum('value')).get('sum_value'))

    pending = self.receivable_set.filter(received=True, date__gte=self.balance_date)
    if pending.count() > 0:
      balance += Decimal(pending.aggregate(sum_value=models.Sum('value')).get('sum_value'))

    return balance
  actual_balance.short_description = "Saldo"

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = "conta"
    verbose_name_plural = "contas"

class Montly(models.Model):
  description = models.CharField(max_length=250)
  value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u"Valor")
  signal = models.CharField(max_length=1, choices=(('R', 'Receita'),('D', 'Despesa')), verbose_name=u"Sinal")
  account = models.ForeignKey(Account, verbose_name=u"Conta")

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = "mensal"
    verbose_name_plural = "mensais"


class Item(models.Model):
  description = models.CharField(max_length=250)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = "item"
    verbose_name_plural = "itens"

class Payable(models.Model):
  parcel = models.IntegerField(default=1, verbose_name=u"Parcela")
  value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name=u"Valor")
  date = models.DateField(verbose_name=u"Data")
  description = models.TextField(verbose_name=u"Descrição")
  tags = models.CharField(max_length=250, verbose_name=u"Tags", blank=True)
  item = models.ForeignKey(Item, verbose_name=u"Item")
  account = models.ForeignKey(Account, verbose_name=u"Conta")
  paid = models.BooleanField(default=False, verbose_name=u"Pago?")

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = "despesa"
    verbose_name_plural = "despesas"


class Receivable(models.Model):
  parcel = models.IntegerField(default=1, verbose_name=u"Parcela")
  value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name=u"Valor")
  date = models.DateField(verbose_name=u"Data")
  description = models.TextField(verbose_name=u"Descrição")
  tags = models.CharField(max_length=250, verbose_name=u"Tags", blank=True)
  item = models.ForeignKey(Item, verbose_name=u"Item")
  account = models.ForeignKey(Account, verbose_name=u"Conta")
  received = models.BooleanField(default=False, verbose_name=u"Recebido?")

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = "receita"
    verbose_name_plural = "receitas"