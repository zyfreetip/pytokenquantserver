from django.contrib import admin
from .models import BlockUser

class BlockUserAdmin(admin.ModelAdmin):
    list_filter = ('is_staff', )
    search_fields = ('username', 'email', 'misc')

admin.site.register(BlockUser, BlockUserAdmin)
