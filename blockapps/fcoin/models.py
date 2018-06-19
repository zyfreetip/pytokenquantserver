#encoding=utf8
from django.db import models
from django.utils import timezone
from djcom.admin_perms import PermissionsMixin
from djcom.utils import dt1970

class MarketTradeOrderModel(PermissionsMixin):
    SIDE_CHOICES_SELL = 0
    SIDE_CHOICES_BUY = 1
    SIDE_CHOICES = (
                (SIDE_CHOICES_SELL, '卖出'),
                (SIDE_CHOICES_BUY, '买入')
            )
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'fcoin'
        db_table = 'market_trade_order'
        managed = True
        verbose_name = u'fcoin market trade order'

    trade_id = models.BigIntegerField(verbose_name='Trade Id', primary_key=True)
    symbol = models.CharField(max_length=255, verbose_name='交易对', default='')
    price = models.DecimalField(max_digits=40, decimal_places=9, verbose_name='成交价格', default=0)
    amount = models.DecimalField(max_digits=40, decimal_places=9, verbose_name='成交数量', default=0)
    timestamp = models.BigIntegerField(verbose_name='timestamp', default=0)
    side = models.CharField(max_length=255, verbose_name='成交类型', choices=SIDE_CHOICES, default=SIDE_CHOICES_SELL)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

    def __str__(self):
        return 'trade_id(%s) symbol(%s) price(%s) amount(%s) side(%s)' % \
            (self.trade_id, self.symbol, self.price, self.amount, self.side)
