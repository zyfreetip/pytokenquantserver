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
