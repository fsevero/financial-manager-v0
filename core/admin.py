from django.contrib import admin
from core.models import Account, Montly, Item, Payable, Receivable


class MontlyAdmin(admin.ModelAdmin):
  list_display = ['description', 'account', 'value', 'signal']
  list_filter = ['signal', 'account']

  def get_queryset(self, request):
    qs = super(MontlyAdmin, self).get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(account__user=request.user)

class AccountAdmin(admin.ModelAdmin):
  list_display = ['description', 'actual_balance', 'income', 'expenses', 'disponible', 'pending_cpa', 'pending_cre']

  def get_queryset(self, request):
    qs = super(AccountAdmin, self).get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(user=request.user)

admin.site.register(Account, AccountAdmin)
admin.site.register(Montly, MontlyAdmin)

class PayableAdmin(admin.ModelAdmin):
  list_display = ['account', 'item', 'value', 'date', 'paid']
  list_filter = ['account', 'paid', 'date']

  def get_queryset(self, request):
    qs = super(PayableAdmin, self).get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(account__user=request.user)

admin.site.register(Item)
admin.site.register(Payable, PayableAdmin)


class ReceivableAdmin(admin.ModelAdmin):
  list_display = ['account', 'item', 'value', 'date', 'received']
  list_filter = ['account', 'received', 'date']

  def get_queryset(self, request):
    qs = super(ReceivableAdmin, self).get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(account__user=request.user)

admin.site.register(Receivable, ReceivableAdmin)