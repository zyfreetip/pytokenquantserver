#encoding=utf8
from django.db import models
from django.utils import timezone
from djcom.admin_perms import PermissionsMixin
from djcom.utils import dt1970

class EthereumBlockModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'ethereum'
        db_table = 'ethereum_block'
        managed = True
        verbose_name = u'以太坊区块表'

    number = models.BigIntegerField(primary_key=True) # BigIntegerField
    hash = models.CharField(max_length=255, verbose_name='区块哈希', default='')
    parent_hash = models.CharField(max_length=255, verbose_name='父哈希', default='')
    nonce = models.CharField(max_length=255, verbose_name='随机数', default=0)
    transactions_root = models.CharField(max_length=255, verbose_name='根交易字典树', default='')
    state_root = models.CharField(max_length=255, verbose_name='根状态字典树', default='')
    receipts_root = models.CharField(max_length=255, verbose_name='根收据字典树', default='')
    miner = models.CharField(max_length=255, verbose_name='矿工', default='')
    difficulty = models.BigIntegerField(verbose_name='该区块难度', default=0)
    total_difficulty = models.CharField(max_length=255, verbose_name='区块累计总难度', default=0)
    extra_data = models.CharField(max_length=255, verbose_name='区块额外信息', default='')
    size = models.BigIntegerField(verbose_name='区块字节数', default=0)
    gas_limit = models.BigIntegerField(verbose_name='gas上限', default=0)
    gas_used = models.CharField(max_length=255, verbose_name='该区块gas使用总量', default=0)
    timestamp = models.BigIntegerField(verbose_name='区块创建时间戳', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

    def __str__(self):
        return 'number(%s) hash(%s) parentHash(%s) miner(%s)' % \
            (self.number, self.hash, self.parent_hash, self.miner)

class EthereumAddressModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'ethereum'
        db_table = 'ethereum_address'
        managed = True
        verbose_name = u'以太坊地址余额表'

    address = models.CharField(max_length=255, primary_key=True)
    received = models.CharField(max_length=255, verbose_name='总接收数量', default='')
    sent = models.CharField(max_length=255, verbose_name='总支出数量', default='')
    balance = models.CharField(max_length=255, verbose_name='当前余额', default=0)
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

class EthereumTransactionModel(PermissionsMixin):

    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'ethereum'
        db_table = 'ethereum_transaction'
        managed = True
        verbose_name = u'以太坊交易记录表'

    txhash = models.CharField(max_length=255, verbose_name='交易哈希', primary_key=True)
    nonce = models.BigIntegerField(verbose_name='随机数', default=0)
    block_hash = models.CharField(max_length=255, verbose_name='区块哈希', default='')
    block_number = models.BigIntegerField(verbose_name='区块高度', default=0)
    txindex = models.BigIntegerField(verbose_name='交易序号', default=0)
    from_address = models.CharField(max_length=255, verbose_name='发送方地址', default='')
    to_address = models.CharField(max_length=255, verbose_name='接收方地址', default='')
    value = models.CharField(max_length=255, verbose_name='交易金额Wei', default=0)
    gas_price = models.CharField(max_length=255, verbose_name='gas价格', default=0)
    gas = models.BigIntegerField(verbose_name='gas数量', default=0)
    input_data = models.TextField(verbose_name='交易发送的数据', default='')
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

    def __str__(self):
        return 'txhash(%s) from_address(%s) to_address(%s) value(%s)' % \
            (self.txhash, self.from_address, self.to_address, self.value)
            
class EthereumTransactionReceiptModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'ethereum'
        db_table = 'ethereum_transaction_receipt'
        managed = True
        verbose_name = u'以太坊交易收据表'
        
    txhash = models.CharField(max_length=255, verbose_name='交易哈希', primary_key=True)
    txindex = models.BigIntegerField(verbose_name='交易序号', default=0)
    block_hash = models.CharField(max_length=255, verbose_name='区块哈希', default='')
    block_number = models.BigIntegerField(verbose_name='区块高度', default=0)
    total_gas = models.CharField(max_length=255, verbose_name='区块gas使用总量', default=0)
    gas_used = models.CharField(max_length=255, verbose_name='该交易使用gas量', default=0)
    contract_address = models.CharField(max_length=255, verbose_name='合约地址', default='')
    root = models.CharField(max_length=255, verbose_name='拜占庭交易状态根', default='')
    status = models.BigIntegerField(verbose_name='状态', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    
    def __str__(self):
        return 'txhash(%s) txindex(%s) gas(%s) contract_address(%s) status(%s)' %\
        (self.txhash, self.txindex, self.gas_used, self.contract_address, self.status)

class EthereumStatsModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'ethereum'
        db_table = 'ethereum_stats'
        managed = True
        verbose_name = u'以太坊指标表'
    
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
        return 'blocks_last_24h(%s) blocks_avg_perhour(%s)'%\
            (self.blocks_last_24h, self.blocks_avg_perhour)
