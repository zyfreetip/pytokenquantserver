#encoding=utf8
from django.db import models
from django.utils import timezone
from djcom.admin_perms import PermissionsMixin
from djcom.utils import dt1970

class QuantPolicy(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        #app_label = 'quant'
        db_table = 'quant_policy'
        managed = True
        verbose_name = u'quant_policy'
 
    title = models.CharField(max_length=255, verbose_name='商品名称', default='')
    price = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='购买价格', default=0)
    content = models.TextField(verbose_name='内容', default='')
    exchanges = models.TextField(verbose_name='支持交易所列表', default='')
    #symbols = models.IntegerField(verbose_name='支持交易对', default=0)
    status = models.IntegerField(verbose_name='状态', default=0)
    update_time = models.DateTimeField(verbose_name='记录更新时间', auto_now=True)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    
    def __str__(self):
        return 'title(%s) price(%s) exchange(%s) ' % \
                           (self.title, self.price, self.exchanges)
                
