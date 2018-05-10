#encoding=utf8
from django.db import models
from django.utils import timezone
from djcom.admin_perms import PermissionsMixin
from djcom.utils import dt1970

class IcoDataModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'icoinfo'
        db_table = 'ico_data'
        managed = True
        verbose_name = u'ico数据表'

    ico_name = models.CharField(max_length=255, verbose_name='项目名称', default='')
    token = models.CharField(max_length=255, verbose_name='项目token代号', default='')
    price = models.CharField(max_length=255, verbose_name='公募成本价', default='')
    country = models.CharField(max_length=255, verbose_name='国家', default='')
    country_cn = models.CharField(max_length=255, verbose_name='国家中文名字', default='')
    tokens = models.CharField(max_length=255, verbose_name='代币总量', default='')
    token_type = models.CharField(max_length=255, verbose_name='代币类型', default='')
    hardcap = models.CharField(max_length=255, verbose_name='硬上限', default='')
    softcap = models.CharField(max_length=255, verbose_name='软上限', default='')
    raised = models.CharField(max_length=255, verbose_name='募集金额(usd)', default='')
    platform = models.CharField(max_length=255, verbose_name='平台', default='')
    distributed = models.CharField(max_length=255, verbose_name='公募百分比', default='')
    ico_start = models.DateTimeField(verbose_name='ico开始时间', default=dt1970())
    ico_end = models.DateTimeField(verbose_name='ico结束时间', default=dt1970())
    category = models.CharField(max_length=255, verbose_name='分类目录', default='')
    url = models.CharField(max_length=255, verbose_name='官网地址', default='')
    tagline = models.CharField(max_length=255, verbose_name='简介', default='')
    intro = models.TextField(verbose_name='介绍', default='')
    intro_cn = models.TextField(verbose_name='中文介绍', default='')
    registration = models.CharField(max_length=255, verbose_name='注册类型', default='')
    status = models.CharField(max_length=255, verbose_name='项目状态', default='')
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

    def __str__(self):
        return 'ico_name(%s) token(%s) price(%s) country(%s)' % \
            (self.ico_name, self.token, self.price, self.country)

class IcoSocialMediaModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'icoinfo'
        db_table = 'ico_social_medial'
        managed = True
        verbose_name = u'社交媒体指标表'
        
    ico_name = models.CharField(max_length=255, verbose_name='项目名称', default='')
    token = models.CharField(max_length=255, verbose_name='项目代号', default='')
    reddit_subscribers = models.IntegerField(verbose_name='reddit订阅数', default=0)
    twitter_followers = models.IntegerField(verbose_name='twitter订阅数', default=0)
    twitter_per_day = models.IntegerField(verbose_name='每日推文数', default=0)
    weibo_post = models.IntegerField(verbose_name='微博数', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    
    def __str__(self):
        return 'ico social media ico_name(%s) token(%s) reddit_subscribers(%s) twitter_per_day(%s)' % \
            (self.ico_name, self.token, self.reddit_subscribers, self.twitter_followers, self.twitter_per_day)

class IcoGithubStatsModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'icoinfo'
        db_table = 'ico_github_stats'
        managed = True
        verbose_name = u'github统计表'
        
    ico_name = models.CharField(max_length=255, verbose_name='项目名称', default='')
    token = models.CharField(max_length=255, verbose_name='项目代号', default='')
    release = models.CharField(max_length=255, verbose_name='版本信息', default='')
    stars = models.IntegerField(verbose_name='stars个数', default=0)
    stars_incr_week = models.IntegerField(verbose_name='本周新增星数', default=0)
    commits_this_month = models.IntegerField(verbose_name='近一个月提交次数', default=0)
    commits_last_week = models.IntegerField(verbose_name='上周提交次数', default=0)
    commits_this_week = models.IntegerField(verbose_name='本周提交次数', default=0)
    codes_this_month = models.IntegerField(verbose_name='近一个月代码提交量', default=0)
    codes_last_week = models.IntegerField(verbose_name='上周代码提交量', default=0) 
    codes_this_week = models.IntegerField(verbose_name='本周代码提交量', default=0) 
    branches = models.IntegerField(verbose_name='分支数', default=0)
    forks = models.IntegerField(verbose_name='fork数', default=0)
    issues = models.IntegerField(verbose_name='问题数', default=0)
    watchers = models.IntegerField(verbose_name='关注数', default=0)
    projects = models.TextField(verbose_name='项目库', default='')
    project_create_time = models.DateTimeField(verbose_name='项目创建时间', default=dt1970()) 
    project_update_time = models.DateTimeField(verbose_name='最后提交时间', default=dt1970())
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    
    def __str__(self):
        return 'github stats ico_name(%s) token(%s) release(%s)' % \
            (self.ico_name, self.token, self.release)

class IcoExchangesStatsModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'icoinfo'
        db_table = 'ico_exchanges_stats'
        managed = True
        verbose_name = u'ico交易所统计表'
        
    ico_name = models.CharField(max_length=255, verbose_name='项目名称', default='')
    token = models.CharField(max_length=255, verbose_name='项目代号', default='')
    fair_price = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='公允价格', default=0)
    change_24h = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='24小时变化百分比', default=0)
    circulating_supply = models.BigIntegerField(verbose_name='已供应币数', default=0)
    max_supply = models.BigIntegerField(verbose_name='总供应币数', default=0)
    market_capitalization = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='市值', default=0)
    transactions_last_24h = models.BigIntegerField(verbose_name='24小时交易量', default=0)
    total_trade_volume_24h = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='24小时交易所成交总额', default=0)    
    turnover_rate = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='换手率', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
    
    def __str__(self):
        return 'ico exchanges stats ico_name(%s) token(%s) fair_price(%s)' % \
            (self.ico_name, self.token, self.fair_price)

class IcoBasicInfoModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'icoinfo'
        db_table = 'ico_basic_info'
        managed = True
        verbose_name = u'ico基本信息表'
    
    ico_name = models.CharField(max_length=255, verbose_name='项目名称', default='')
    token = models.CharField(max_length=255, verbose_name='项目代号', default='')
    category = models.CharField(max_length=255, verbose_name='类别（可挖不可挖矿平台币应用币）', default='')
    first_block_time = models.DateTimeField(verbose_name='第一个区块生成时间', default=dt1970())
    ico_price = models.CharField(max_length=255, verbose_name='ico价格', default='')
    total_volumn = models.BigIntegerField(verbose_name='币总量', default=0)
    maximum_tps = models.CharField(max_length=255, verbose_name='最大每秒传输量', default='')
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)
 
    def __str__(self):
        return 'ico basic info ico_name(%s) token(%s)' % \
            (self.ico_name, self.token)

class IcoStatsModel(PermissionsMixin):
    class Meta(PermissionsMixin.Meta):
        abstract = False
        app_label = 'icoinfo'
        db_table = 'ico_stats'
        managed = True
        verbose_name = u'ico指标表'
    
    ico_name = models.CharField(max_length=255, verbose_name='项目名称', default='')
    token = models.CharField(max_length=255, verbose_name='项目代号', default='')
    transactions_number_day = models.BigIntegerField(verbose_name='当日总交易次数', default=0)
    transactions_number_hour = models.BigIntegerField(verbose_name='小时总交易次数', default=0)
    total_transactions_fees = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='当日总交易费', default=0)
    avg_transactions_value = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='交易价值均值', default=0)
    meidan_transactions_value = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='交易价值中位数', default=0)
    total_output_value = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='当日总交易传出量', default=0)
    assets_turnover_rate = models.DecimalField(max_digits=40, decimal_places=5, verbose_name='资产中转率', default=0)
    actual_tps = models.BigIntegerField(verbose_name='实际每秒交易量', default=0)
    tps_utilization_rate = models.DecimalField(verbose_name='tps利用率', max_digits=40, decimal_places=5, default=0)
    median_confirmation_time = models.DateTimeField(verbose_name='确认时间中位数', default=dt1970())
    mempool_size = models.BigIntegerField(verbose_name='未确认交易数量', default=0)
    current_best_transaction_fees = models.DecimalField(verbose_name='最佳交易费用', max_digits=40, decimal_places=5, default=0)
    blocks_last_24h = models.BigIntegerField(verbose_name='24小时生成区块数', default=0)
    blocks_avg_perhour = models.BigIntegerField(verbose_name='每小时生成区块数', default=0)
    block_time = models.CharField(verbose_name='平均区块生成时间', max_length=255, default='')
    difficulty = models.CharField(verbose_name='难度', max_length=255, default='')
    hashrate = models.CharField(verbose_name='算力', max_length=255, default='')
    blocks_mined_day = models.CharField(verbose_name='当天挖出区块', max_length=255, default='')
    bitcoins_mined_total = models.CharField(verbose_name='累计挖出比特币数量', max_length=255, default='')
    block_count = models.BigIntegerField(verbose_name='区块总数',  default=0)
    block_pre_reward = models.DecimalField(verbose_name='当前区块奖励数', max_digits=40, decimal_places=5, default=0)
    reward_last_24h = models.DecimalField(verbose_name='24小时区块奖励数', max_digits=40, decimal_places=5, default=0)
    top_100_richest = models.BigIntegerField(verbose_name='前100占有币情况', default=0)
    wealth_distribution_top10 = models.BigIntegerField(verbose_name='财富10', default=0)
    wealth_distribution_top100 = models.BigIntegerField(verbose_name='财富100', default=0)
    wealth_distribution_top1000 = models.BigIntegerField(verbose_name='财富1000', default=0)
    wealth_distribution_top10000 = models.BigIntegerField(verbose_name='财富10000', default=0)
    address_richer_than_1usd = models.BigIntegerField(verbose_name='金额超过1usd地址', default=0)
    address_richer_than_100usd = models.BigIntegerField(verbose_name='金额超过100usd地址', default=0)
    address_richer_than_1000usd = models.BigIntegerField(verbose_name='金额超过1000usd地址', default=0)
    address_richer_than_10000usd = models.BigIntegerField(verbose_name='金额超过10000usd地址', default=0)
    active_addresses_last24h = models.BigIntegerField(verbose_name='过去24小时活跃地址数', default=0)
    new_addresses_last24h = models.BigIntegerField(verbose_name='过去24小时新建地址数', default=0)
    transaction_largest100 = models.BigIntegerField(verbose_name='24小时最大100笔交易', default=0)
    mining_pro = models.CharField(verbose_name='24小时矿工收入', max_length=255, default='')
    transactions_fees = models.CharField(verbose_name='交易费用百分比', max_length=255, default='')
    per_transactions_volume = models.CharField(verbose_name='矿工收入/交易量', max_length=255, default='')
    cost_per_transaction = models.CharField(verbose_name='平均每次交易成本(usd)', max_length=255, default='')
    mining_pro_1thash = models.CharField(verbose_name='1thash/s的算力估计收益', max_length=255, default='')
    address_numbers = models.BigIntegerField(verbose_name='持币地址数', default=0)
    create_time = models.DateTimeField(verbose_name='记录创建时间', auto_now_add=True)

    def __str__(self):
        return 'blocks_last_24h(%s) blocks_avg_perhour(%s)' %\
            (self.blocks_last_24h, self.blocks_avg_perhour)
