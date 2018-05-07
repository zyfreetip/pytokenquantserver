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
