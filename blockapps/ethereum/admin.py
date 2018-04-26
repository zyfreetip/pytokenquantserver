from django.contrib import admin
from djcom.utils import registerAdminFromModels
from . import models 
from djcom.admin_perms import PermModelAdmin

class EthereumBlockModelAdmin(PermModelAdmin):
    search_fields = ('number',)

admin.site.register(models.EthereumBlockModel, EthereumBlockModelAdmin)
registerAdminFromModels(models)