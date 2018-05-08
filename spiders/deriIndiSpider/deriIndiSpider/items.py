# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from ethereum.models import EthereumStatsModel
from btc.models import BtcStatsModel
from icoinfo.models import IcoDataModel
from icoinfo.models import IcoStatsModel


class DeriBtcSpiderItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = BtcStatsModel


class DeriEthSpiderItem(DjangoItem):
    django_model = EthereumStatsModel

class IcoInfoSpiderItem(DjangoItem):
    django_model = IcoDataModel

class IcoStatsItem(DjangoItem):
    django_model = IcoStatsModel