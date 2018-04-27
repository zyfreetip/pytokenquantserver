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
        verbose_name = u'比特币区块表'

    height = models.BigIntegerField(primary_key=True) # BigIntegerField
    weight = models.BigIntegerField(verbose_name='区块重量', default=0)
    version = models.IntegerField(verbose_name='版本号', default=0)
    mrkl_root = models.CharField(max_length=255, verbose_name='Merkle Root', default='')
    curr_max_timestamp = models.BigIntegerField(verbose_name='块最大时间戳', default=0)
    timestamp = models.BigIntegerField(verbose_name='块时间戳', default=0)
    bits = models.CharField(max_length=255, verbose_name='bits', default='')
    nonce = models.BigIntegerField(verbose_name='随机数', default=0)
    hash = models.CharField(max_length=255, verbose_name='块哈希', default='')
    prev_block_hash = models.CharField(max_length=255, verbose_name='前向区块哈希', default='')
    next_block_hash = models.CharField(max_length=255, verbose_name='后向区块哈希', default='')
    size = models.BigIntegerField(verbose_name='区块体积', default=0)
    pool_difficulty = models.BigIntegerField(verbose_name='矿池难度', default=0)
    difficulty = models.BigIntegerField(verbose_name='块难度', default=0)
    tx_count = models.BigIntegerField(verbose_name='交易数量', default=0)
    reward_block = models.BigIntegerField(verbose_name='块奖励', default=0)
    reward_fees = models.BigIntegerField(verbose_name='块手续费', default=0)
    confirmations = models.IntegerField(verbose_name='确认数', default=0)
    relayed_by = models.CharField(max_length=255, verbose_name='块播报方', default='')
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

class BtcTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'btc'
        db_table = 'btc_transaction'
        managed = True
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
    
    def __str_(self):
        return 'txhash(%s) block_height(%s) fee(%s)' %\
            (self.txhash, self.block_height, self.fee)
class BtcInputTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label ='btc'
        db_table = 'btc_input_transaction'
        managed = True
        verbose_name = u'比特币输入交易记录表'
    
    txhash = models.CharField(max_length=255, verbose_name='交易hash', default='')
    prev_address = models.CharField(max_length=255, verbose_name='输入地址', default='')
    prev_position = models.BigIntegerField(verbose_name='前向交易的输出位置', default=0)
    prev_value = models.BigIntegerField(verbose_name='前向交易输入金额', default=0)
    prev_tx_hash = models.CharField(verbose_name='前向交易哈希', max_length=255, default='')
    script_asm = models.CharField(verbose_name='asm脚本', max_length=255, default='')
    script_hex = models.CharField(verbose_name='hex脚本', max_length=255, default='')
    sequence = models.BigIntegerField(verbose_name='序列', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    
    def __str__(self):
        return 'txhash(%s) prev_address(%s)' %\
            (self.txhash, self.prev_address)

class BtcOutputTransactionModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label ='btc'
        db_table = 'btc_output_transaction'
        managed = True
        verbose_name = u'比特币输出交易记录表'
    
    txhash = models.CharField(max_length=255, verbose_name='交易hash', default='')
    address = models.CharField(max_length=255, verbose_name='输出地址', default='')
    value = models.BigIntegerField(verbose_name='输出金额', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

    def __str__(self):
        return 'txhash(%s) address(%s)' %\
            (self.txhash, self.address)

class BtcStatsModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'btc'
        db_table = 'btc_stats'
        managed = True
        verbose_name = u'比特币指标表'
    
    blocks_last_24h = models.BigIntegerField(verbose_name='24小时生成区块数', default=0)
    blocks_avg_perhour = models.BigIntegerField(verbose_name='每小时生成区块数', default=0)
    reward_last_24h = models.BigIntegerField(verbose_name='24小时产生奖励数', default=0)
    top_100_richest = models.BigIntegerField(verbose_name='前100占有币情况', default=0)
    wealth_distribution_top10 = models.BigIntegerField(verbose_name='财富10', default=0)
    wealth_distribution_top100 = models.BigIntegerField(verbose_name='财富100', default=0)
    wealth_distribution_top1000 = models.BigIntegerField(verbose_name='财富1000', default=0)
    wealth_distribution_top10000 = models.BigIntegerField(verbose_name='财富10000', default=0)
    address_richer_than_1usd = models.BigIntegerField(verbose_name='金额超过1usd地址', default=0)
    address_richer_than_100usd = models.BigIntegerField(verbose_name='金额超过100usd地址', default=0)
    address_richer_than_1000usd = models.BigIntegerField(verbose_name='金额超过1000usd地址', default=0)
    address_richer_than_10000usd = models.BigIntegerField(verbose_name='金额超过10000usd地址', default=0)
    active_addresses_last24h = models.BigIntegerField(verbose_name='24小时活跃地址数', default=0)
    transaction_largest100 = models.BigIntegerField(verbose_name='24小时最大100笔交易', default=0)
    address_numbers = models.BigIntegerField(verbose_name='持币地址数', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    total = models.BigIntegerField(verbose_name='币总量', default=0)

    def __str__(self):
        return 'blocks_last_24h(%s) blocks_avg_perhour(%s)' %\
            (self.blocks_last_24h, self.blocks_avg_perhour)
    
