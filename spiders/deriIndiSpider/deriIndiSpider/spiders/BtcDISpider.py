from scrapy.spiders import Spider
from scrapy import Request
from deriIndiSpider.items import DeriBtcSpiderItem

import re
import datetime
from django.utils import timezone
import time

class BtcDiSpider(Spider):
    name = 'btc_di'
    
    def __init__(self):
        self.coin_name = 'coin c_btc'

    def start_requests(self):
        url = 'https://bitinfocharts.com'
        yield Request(url)

    def handle_string(self, content, rtype=0):
        number_list = re.findall(r'\d+\.?\d*', content)
        target = ''
        for single in number_list:
            target += single
        if rtype == 0:
            number = int(target)
        elif rtype == 1:
            number = float(target)
        return number

    def handle_string_mulpercentage(self, content):
        number_list = re.findall(r'\d+\.?\d*', content)
        return number_list

    def handle_string_2(self, content):
        number_str_list = content.split('/')
        numbers = []
        for item in number_str_list:
            item_num = self.handle_string(item)
            numbers.append(item_num)
        return numbers

    def parse(self, response):

        print("开始获取相关信息 in ", time.asctime( time.localtime(time.time())))
        item = DeriBtcSpiderItem()
        blocks_last_24h = response.xpath('//tr[@id="t_blocks24"]/td[@class="'+self.coin_name+'"]/text()').extract()[0]

        item['blocks_last_24h'] = self.handle_string(blocks_last_24h)

        blocks_avg_perhour = response.xpath('//tr[@id="t_blocksPerH"]/td[@class="'+self.coin_name+'"]/text()').extract()[0]
        item['blocks_avg_perhour'] = self.handle_string(blocks_avg_perhour)


        rewards_abbr  = response.xpath('//tr[@class="t_empty" and td[text()="Reward last 24h"]]/td[@class="'+self.coin_name+'"]/span/abbr')
        reward_last_24h = self.handle_string(rewards_abbr[0].xpath("./text()").extract()[0], rtype=1) * 100000000+\
                          self.handle_string(rewards_abbr[1].xpath("./text()").extract()[0], rtype=1) * 100000000
        item['reward_last_24h'] =int(reward_last_24h)

        top_100_richest =response.xpath('//tr[@class="t_empty" and td[text()="Top 100 Richest"]]/td[@class="'+self.coin_name+'"]/a/span/text()').extract()[0]
        top_100_richest = self.handle_string(top_100_richest)
        item['top_100_richest'] = top_100_richest

        wealth_distribution_list = response.xpath('//tr[@class="t_empty" and td[text()="Wealth Distribution"]]/td[@class="'+self.coin_name+'"]/text()').extract()[0]
        wealth_distribution_list = self.handle_string_mulpercentage(wealth_distribution_list)
        wealth_distribution_list = [int(float(i)*100) for i in wealth_distribution_list]

        wealth_distribution_top10 = wealth_distribution_list[0]
        item['wealth_distribution_top10'] = wealth_distribution_top10

        wealth_distribution_top100 = wealth_distribution_list[1]
        item['wealth_distribution_top100'] = wealth_distribution_top100

        wealth_distribution_top1000 = wealth_distribution_list[2]
        item['wealth_distribution_top1000'] = wealth_distribution_top1000

        wealth_distribution_top10000 = wealth_distribution_list[3]
        item['wealth_distribution_top10000'] = wealth_distribution_top10000

        address_richer_than_list_str = response.xpath('//tr[@class="t_empty" and td[text()="Addresses richer than"]]/td[@class="'+self.coin_name+'"]/text()').extract()[0]
        address_richer_than_list = self.handle_string_2(address_richer_than_list_str)

        address_richer_than_1usd = address_richer_than_list[0]
        item['address_richer_than_1usd'] = address_richer_than_1usd

        address_richer_than_100usd = address_richer_than_list[1]
        item['address_richer_than_100usd'] = address_richer_than_100usd

        address_richer_than_1000usd = address_richer_than_list[2]
        item['address_richer_than_1000usd'] = address_richer_than_1000usd

        address_richer_than_10000usd = address_richer_than_list[3]
        item['address_richer_than_10000usd'] = address_richer_than_10000usd

        active_addresses_last24h = response.xpath('//tr[@class="t_empty" and td/a[text()="Active Addresses last 24h"]]/td[@class="'+self.coin_name+'"]/a/text()').extract()[0]
        active_addresses_last24h = self.handle_string(active_addresses_last24h)
        item['active_addresses_last24h'] = active_addresses_last24h

        transaction_largest100 =  response.xpath('//tr[@class="t_empty" and td[text()="100 Largest Transactions"]]/td[@class="'+self.coin_name+'"]/span/text()').extract()[0]
        item['transaction_largest100'] = self.handle_string(transaction_largest100) * 100000000
        # address_numbers = response.xpath('').extract()[0]
        total = response.xpath('//tr[@id="t_total"]/td[@class="'+self.coin_name+'"]/text()').extract()[0]
        item['total'] = self.handle_string(total)
        item['create_time'] = timezone.now()
        print(item)
        yield item
