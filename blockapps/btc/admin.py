from django.contrib import admin
from djcom.utils import registerAdminFromModels
from . import models 
from djcom.admin_perms import PermModelAdmin

class BtcBlockModelAdmin(PermModelAdmin):
    search_fields = ('height',)

admin.site.register(models.BtcBlockModel, BtcBlockModelAdmin)
registerAdminFromModels(models)
