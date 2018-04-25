#encoding=utf8
from django.db import models
from django.utils import timezone
from djcom.admin_perms import PermissionsMixin
from djcom.utils import dt1970

class BtcBlockModel(PermissionsMixin):

    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'btc'
        db_table = 'btc_block'
        managed = True

    height = models.BigIntegerField(primary_key=True) # BigIntegerField
    weight = models.BigIntegerField(verbose_name='区块重量')
    version = models.IntegerField(verbose_name='版本号')
    mrkl_root = models.CharField(max_length=255, verbose_name='Merkle Root', default='')
    curr_max_timestamp = models.BigIntegerField(verbose_name='块最大时间戳')
    timestamp = models.BigIntegerField(verbose_name='块时间戳')
    bits = models.CharField(max_length=255, verbose_name='bits')
    nonce = models.BigIntegerField(verbose_name='随机数')
    hash = models.CharField(max_length=255, verbose_name='快哈希')
    prev_block_hash = models.CharField(max_length=255, verbose_name='前向区块哈希')
    next_block_hash = models.CharField(max_length=255, verbose_name='后向区块哈希')
    size = models.BigIntegerField(verbose_name='区块体积')
    pool_difficulty = models.BigIntegerField(verbose_name='矿池难度')
    difficulty = models.BigIntegerField(verbose_name='块难度')
    tx_count = models.BigIntegerField(verbose_name='交易数量')
    reward_block = models.BigIntegerField(verbose_name='块奖励')
    reward_fees = models.BigIntegerField(verbose_name='块手续费')
    confirmations = models.IntegerField(verbose_name='确认数')
    relayed_by = models.CharField(max_length=255, verbose_name='块播报方')
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

    def __str__(self):
        return 'height(%s) size(%s) tx_count(%s) relayed_by(%s)' % \
            (self.height, self.size, self.tx_count, self.relayed_by)

class BtcAddressModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'btc'
        db_table = 'btc_address'
        managed = True
    
    address = models.CharField(max_length=255, primary_key=True)
    received = models.BigIntegerField(verbose_name='总接收数量')
    sent = models.BigIntegerField(verbose_name='总支出数量')
    balance = models.BigIntegerField(verbose_name='当前余额')
    tx_count = models.BigIntegerField(verbose_name='交易数量')
    unconfirmed_tx_count = models.BigIntegerField(verbose_name='未确认交易数量')
    unconfirmed_rx_count = models.BigIntegerField(verbose_name='未确认总接收')
    unconfirmed_sent = models.BigIntegerField(verbose_name='未确认总支出')
    unspent_tx_count = models.BigIntegerField(verbose_name='未花费交易数量')
    create_time = models.DateTimeField(verbose_name='记录创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)

class BtcTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'btc'
        db_table = 'btc_transaction'
        managed = True
        
    txhash = models.CharField(max_length=255, primary_key=True)
    block_height = models.BigIntegerField(verbose_name='所在块高度')
    block_time = models.BigIntegerField(verbose_name='所在块时间')
    fee = models.BigIntegerField(verbose_name='交易手续费')
    inputs_count = models.BigIntegerField(verbose_name='输入数量')
    inputs_value = models.BigIntegerField(verbose_name='输入金额')
    is_coinbase = models.BooleanField(verbose_name='是否为coinbase交易')
    lock_time = models.BigIntegerField(verbose_name='锁定时间')
    outputs_count = models.BigIntegerField(verbose_name='输出数量')
    outputs_value = models.BigIntegerField(verbose_name='输出金额')
    size = models.BigIntegerField(verbose_name='交易体积')
    version = models.BigIntegerField(verbose_name='交易版本号')
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

class BtcInputTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label ='btc'
        db_table = 'btc_input_transaction'
        managed = True
    
    txhash = models.CharField(max_length=255, verbose_name='交易hash')
    prev_address = models.CharField(max_length=255, verbose_name='输入地址')
    prev_position = models.BigIntegerField(verbose_name='前向交易的输出位置')
    prev_value = models.BigIntegerField(verbose_name='前向交易输入金额')
    prev_tx_hash = models.CharField(verbose_name='前向交易哈希', max_length=255)
    script_asm = models.CharField(verbose_name='asm脚本', max_length=255)
    script_hex = models.CharField(verbose_name='hex脚本', max_length=255)
    sequence = models.BigIntegerField(verbose_name='序列')
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

class BtcOutputTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label ='btc'
        db_table = 'btc_output_transaction'
        managed = True
    
    txhash = models.CharField(max_length=255, verbose_name='交易hash')
    address = models.CharField(max_length=255, verbose_name='输出地址')
    value = models.BigIntegerField(verbose_name='输出金额')
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)


class BtcStatsModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'btc'
        db_table = 'btc_stats'
        managed = True
    
    blocks_last_24h = models.BigIntegerField(verbose_name='24小时生成区块数', primary_key=True)
    blocks_avg_perhour = models.BigIntegerField(verbose_name='每小时生成区块数')
    reward_last_24h = models.BigIntegerField(verbose_name='24小时产生奖励数')
    top_100_richest = models.BigIntegerField(verbose_name='前100占有币情况')
    wealth_distribution_top10 = models.BigIntegerField(verbose_name='财富10')
    wealth_distribution_top100 = models.BigIntegerField(verbose_name='财富100')
    wealth_distribution_top1000 = models.BigIntegerField(verbose_name='财富1000')
    wealth_distribution_top10000 = models.BigIntegerField(verbose_name='财富10000')
    address_richer_than_1usd = models.BigIntegerField(verbose_name='金额超过1usd地址')
    address_richer_than_100usd = models.BigIntegerField(verbose_name='金额超过100usd地址')
    address_richer_than_1000usd = models.BigIntegerField(verbose_name='金额超过1000usd地址')
    address_richer_than_10000usd = models.BigIntegerField(verbose_name='金额超过10000usd地址')
    active_addresses_last24h = models.BigIntegerField(verbose_name='24小时活跃地址数')
    transaction_largest100 = models.BigIntegerField(verbose_name='24小时最大100笔交易')
    address_numbers = models.BigIntegerField(verbose_name='持币地址数')
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    total = models.BigIntegerField(verbose_name='币总量')
    
    
    
    
    
    
    
    
    
       
    
