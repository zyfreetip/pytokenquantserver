#encoding=utf8
from django.db import models
from django.utils import timezone
from djcom.admin_perms import PermissionsMixin
from djcom.utils import dt1970
from djcom.admin_perms import PermissionsMixin

class BaseBtcAddressModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = True
        app_label = 'btc'
        db_table = 'btc_address'
        managed = False
        verbose_name = u'比特币地址表'
    
    address = models.CharField(max_length=255, primary_key=True)
    received = models.BigIntegerField(verbose_name='总接收数量', default=0)
    sent = models.BigIntegerField(verbose_name='总支出数量', default=0)
    balance = models.BigIntegerField(verbose_name='当前余额', default=0)
    tx_count = models.BigIntegerField(verbose_name='交易数量', default=0)
    unconfirmed_tx_count = models.BigIntegerField(verbose_name='未确认交易数量', default=0)
    unconfirmed_rx_count = models.BigIntegerField(verbose_name='未确认总接收', default=0)
    unconfirmed_sent = models.BigIntegerField(verbose_name='未确认总支出', default=0)
    unspent_tx_count = models.BigIntegerField(verbose_name='未花费交易数量', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)
    
    def __str__(self):
        return 'address(%s) balance(%s)' % \
            (self.address, self.balance)

class BaseBtcTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = True
        app_label = 'btc'
        db_table = 'btc_transaction'
        managed = False
        verbose_name = u'比特币交易记录表'
        
    txhash = models.CharField(max_length=255, primary_key=True)
    block_height = models.BigIntegerField(verbose_name='所在块高度', default=0)
    block_time = models.BigIntegerField(verbose_name='所在块时间', default=0)
    fee = models.BigIntegerField(verbose_name='交易手续费', default=0)
    inputs_count = models.BigIntegerField(verbose_name='输入数量', default=0)
    inputs_value = models.BigIntegerField(verbose_name='输入金额', default=0)
    is_coinbase = models.BooleanField(verbose_name='是否为coinbase交易', default=0)
    lock_time = models.BigIntegerField(verbose_name='锁定时间', default=0)
    outputs_count = models.BigIntegerField(verbose_name='输出数量', default=0)
    outputs_value = models.BigIntegerField(verbose_name='输出金额', default=0)
    size = models.BigIntegerField(verbose_name='交易体积', default=0)
    version = models.BigIntegerField(verbose_name='交易版本号', default=0)
    confirmations = models.BigIntegerField(verbose_name='确认数', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    
    def __str__(self):
        return 'txhash(%s) block_height(%s) fee(%s)' %\
            (self.txhash, self.block_height, self.fee)
class BaseBtcInputTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = True
        app_label ='btc'
        db_table = 'btc_input_transaction'
        managed = False
        verbose_name = u'比特币输入交易记录表'
    
    txhash = models.CharField(max_length=255, verbose_name='交易hash', default='')
    prev_address = models.CharField(max_length=255, verbose_name='输入地址', default='')
    prev_position = models.BigIntegerField(verbose_name='前向交易的输出位置', default=0)
    prev_value = models.BigIntegerField(verbose_name='前向交易输入金额', default=0)
    prev_tx_hash = models.CharField(verbose_name='前向交易哈希', max_length=255, default='')
    script_asm = models.TextField(verbose_name='asm脚本', default='')
    script_hex = models.TextField(verbose_name='hex脚本', default='')
    sequence = models.BigIntegerField(verbose_name='序列', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    
    def __str__(self):
        return 'txhash(%s) prev_address(%s)' %\
            (self.txhash, self.prev_address)

class BaseBtcOutputTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = True
        app_label ='btc'
        db_table = 'btc_output_transaction'
        managed = False
        verbose_name = u'比特币输出交易记录表'
    
    txhash = models.CharField(max_length=255, verbose_name='交易hash', default='')
    address = models.CharField(max_length=255, verbose_name='输出地址', default='')
    value = models.BigIntegerField(verbose_name='输出金额', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

    def __str__(self):
        return 'txhash(%s) address(%s)' %\
            (self.txhash, self.address)