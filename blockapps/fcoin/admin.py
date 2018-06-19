from django.contrib import admin
from djcom.utils import registerAdminFromModels
from . import models 
from djcom.admin_perms import PermModelAdmin

class MarketTradeModelAdmin(PermModelAdmin):
    search_fields = ('symbol','side','amount')
admin.site.register(models.MarketTradeOrderModel, MarketTradeModelAdmin)
registerAdminFromModels(models)
