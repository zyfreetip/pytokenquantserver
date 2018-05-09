from scrapy.spiders import Spider
from scrapy import Request
from deriIndiSpider.items import DeriBtcSpiderItem
from deriIndiSpider.items import IcoStatsItem

import re
import datetime
from django.utils import timezone
import time


class BitinfoChartSpider(Spider):
    name = 'bitinfo'

    def __init__(self, coin_name=None, *args, **kwargs):
        super(BitinfoChartSpider, self).__init__(*args, **kwargs)
        if coin_name:
            self.coin_name = coin_name
        else:
            print("Please input the coin name")
            return

    def start_requests(self):
        url = 'https://bitinfocharts.com'
        yield Request(url)

    def handle_string(self, content, rtype=0):
        number_list = re.findall(r'\d+\.?\d*', content)
        target = ''
        for single in number_list:
            target += single
        if rtype == 0:
            target = int(target)
        elif rtype == 1:
            target = float(target)
        return target

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

        print("开始获取相关信息 in ", time.asctime(time.localtime(time.time())))
        item = IcoStatsItem()

        # project_name
        try:
            ico_name = response.xpath('//tr[@class="t_coin"]/td[@class="coin c_eth"]/a/text()').extract()[1].strip()
            item['ico_name'] = ico_name
        except IndexError as e:
            print('ico_name', 'not exist in ', self.coin_name)

        # blocks_last_24h
        try:
            blocks_last_24h = response.xpath('//tr[@id="t_blocks24"]/td[@class="' + self.coin_name + '"]/text()').extract()[0]
            item['blocks_last_24h'] = self.handle_string(blocks_last_24h)
        except IndexError as e:
            print("blocks_last_24h not exist in "+self.coin_name)


        #  blocks_avg_perhour
        try:
            blocks_avg_perhour = \
            response.xpath('//tr[@id="t_blocksPerH"]/td[@class="' + self.coin_name + '"]/text()').extract()[0]
            item['blocks_avg_perhour'] = self.handle_string(blocks_avg_perhour)
        except IndexError as e:
            print('blocks_avg_perhour not exist in' + self.coin_name)


        try:
            rewards_abbr = response.xpath(
            '//tr[@class="t_empty" and td[text()="Reward last 24h"]]/td[@class="' + self.coin_name + '"]/span/abbr')
            reward_last_24h = self.handle_string(rewards_abbr[0].xpath("./text()").extract()[0], rtype=1) * 100000000 + \
                          self.handle_string(rewards_abbr[1].xpath("./text()").extract()[0], rtype=1) * 100000000
            item['reward_last_24h'] = int(reward_last_24h)
        except IndexError as e:
            print('reward_abbr not exist in '+ self.coin_name)


        try:
            top_100_richest = response.xpath(
                '//tr[@class="t_empty" and td[text()="Top 100 Richest"]]/td[@class="' + self.coin_name + '"]/a/span/text()').extract()[
                0]
            top_100_richest = self.handle_string(top_100_richest)
            item['top_100_richest'] = top_100_richest
        except IndexError as e:
            print("top_100_richest not exist, ignore")

        try:
            wealth_distribution_list = response.xpath(
                '//tr[@class="t_empty" and td[text()="Wealth Distribution"]]/td[@class="' + self.coin_name + '"]/text()').extract()[
                0]
            wealth_distribution_list = self.handle_string_mulpercentage(wealth_distribution_list)
            wealth_distribution_list = [int(float(i) * 100) for i in wealth_distribution_list]

            wealth_distribution_top10 = wealth_distribution_list[0]
            item['wealth_distribution_top10'] = wealth_distribution_top10

            wealth_distribution_top100 = wealth_distribution_list[1]
            item['wealth_distribution_top100'] = wealth_distribution_top100

            wealth_distribution_top1000 = wealth_distribution_list[2]
            item['wealth_distribution_top1000'] = wealth_distribution_top1000

            wealth_distribution_top10000 = wealth_distribution_list[3]
            item['wealth_distribution_top10000'] = wealth_distribution_top10000
        except IndexError as e :
            print("wealth_distribution_list not exist in "+self.coin_name)

        try:
            address_richer_than_list_str = response.xpath(
                '//tr[@class="t_empty" and td[text()="Addresses richer than"]]/td[@class="' + self.coin_name + '"]/text()').extract()[
                0]
            address_richer_than_list = self.handle_string_2(address_richer_than_list_str)

            address_richer_than_1usd = address_richer_than_list[0]
            item['address_richer_than_1usd'] = address_richer_than_1usd

            address_richer_than_100usd = address_richer_than_list[1]
            item['address_richer_than_100usd'] = address_richer_than_100usd

            address_richer_than_1000usd = address_richer_than_list[2]
            item['address_richer_than_1000usd'] = address_richer_than_1000usd

            address_richer_than_10000usd = address_richer_than_list[3]
            item['address_richer_than_10000usd'] = address_richer_than_10000usd
        except IndexError as e:
            print("address_richer_than_list_str not exist in "+self.coin_name )

        # active_addresses_last24h
        try:
            active_addresses_last24h = response.xpath(
            '//tr[@class="t_empty" and td/a[text()="Active Addresses last 24h"]]/td[@class="' + self.coin_name + '"]/a/text()').extract()[
            0]
            active_addresses_last24h = self.handle_string(active_addresses_last24h)
            item['active_addresses_last24h'] = active_addresses_last24h
        except IndexError as e:
            print("active_addresses_last24h not exist in "+self.coin_name)


        # transaction_largest100
        try:
            transaction_largest100 = response.xpath(
            '//tr[@class="t_empty" and td[text()="100 Largest Transactions"]]/td[@class="' + self.coin_name + '"]/span/text()').extract()[
            0]
            item['transaction_largest100'] = self.handle_string(transaction_largest100) * 100000000
        except IndexError as e:
            print("transaction_largest100 not exist in "+self.coin_name)

        # address_numbers = response.xpath('').extract()[0]

        # try:
        #     total = response.xpath('//tr[@id="t_total"]/td[@class="' + self.coin_name + '"]/text()').extract()[0]
        #     item['total'] = self.handle_string(total)
        # except IndexError as e:
        #     print("total not exist in "+self.coin_name)

        # Transaction last 24h
        try:
            transactions_number_day = response.xpath('//tr[@class="t_empty" and td/a[contains(text(), "Transactions")] and td[contains(text(), " last 24h")]]/td[@class="'+self.coin_name+'"]/a/text()').extract()[0]
            item['transactions_number_day'] =self.handle_string(transactions_number_day)
        except IndexError as e:
            print("transactions last 24h not exist in "+self.coin_name)

        # Transacton average hour
        try:

            transactions_number_hour = response.xpath('//tr[@class="t_empty" and td/a[contains(text(), "Transactions")] and td[contains(text(), " avg. per hour")]]/td[@class="'+self.coin_name+'"]/a/text()').extract()[0]
            item['transactions_number_hour'] = self.handle_string(transactions_number_hour)
        except IndexError as e:
            print("Transactions average not exist in ",self.coin_name)

        # total_output_value 当日交易sent数量
        try:
            total_output_value = response.xpath('//tr[@class="t_empty" and td/a[contains(text(), "Sent")] and td[contains(text(), " last 24h")]]/td[@class="'+self.coin_name+'"]/a/span/text()').extract()[1]
            total_output_value = self.handle_string(total_output_value, rtype=1)
            item['total_output_value'] = total_output_value
        except IndexError as e:
            print('total_output_value not exist in ', self.coin_name)

        # avg_transactions_value
        try:
            avg_transactions_value =  response.xpath('//tr[@class="t_empty" and td[contains(text(), "Avg. Transaction Value")]]/td[@class="'+self.coin_name+'"]/span/text()').extract()[1]
            avg_transactions_value = self.handle_string(avg_transactions_value, rtype=1)
            item['avg_transactions_value'] = avg_transactions_value
        except IndexError as e:
            print("avg_transactions_value not exist in ", self.coin_name)

        # meidan_transactions_value
        try:
            meidan_transactions_value =  response.xpath('//tr[@class="t_empty" and td[contains(text(), "Median Transaction Value")]]/td[@class="'+self.coin_name+'"]/span/text()').extract()[1]
            meidan_transactions_value = self.handle_string(meidan_transactions_value, rtype=1)
            item['meidan_transactions_value'] = meidan_transactions_value
        except IndexError as e:
            print('meidan_transactions_value not exist in ', self.coin_name)

        try:
            block_time = response.xpath('//tr[@id="t_time"]/td[@class="' + self.coin_name + '"]/a/text()').extract()[0]
            item['block_time'] = block_time
        except IndexError as e:
            print('block_time', ' not exist in ', self.coin_name)


        # block_count
        try:
            block_count = response.xpath('//tr[@id="t_blocks"]/td[@class="' + self.coin_name + '"]/text()').extract()[0]
            block_count = self.handle_string(block_count)
            item['block_count'] = block_count
        except IndexError as e:
            print('block count', 'not exist in ', self.coin_name)

        try:
            block_pre_reward = response.xpath('//tr[@class="t_empty" and td[contains(text(), "Reward Per Block")]]/td[@class="'+self.coin_name+'"]/span/text()').extract()[2]
            block_pre_reward = self.handle_string(block_pre_reward, rtype=1)
            item['block_pre_reward'] = float(block_pre_reward)
        except IndexError as e:
            print('block_pre_reward', 'not exist in ', self.coin_name)

        # difficulty
        try:
            difficulty = response.xpath('//tr[@id="t_diff"]/td[@class="'+self.coin_name+'"]/a/text()').extract()[0]
            difficulty = self.handle_string(difficulty)
            item['difficulty'] = difficulty
        except IndexError as e:
            print('difficulty', 'not exist in ', self.coin_name)

        # HashRate
        try:
            hashrate = response.xpath('//tr[@id="t_hash"]/td[@class="'+self.coin_name+'"]/a/abbr/text()').extract()[0]
            item['hashrate'] = hashrate
        except IndexError as e:
            print('hashrate', ' not exist in ', self.coin_name)

        try:
            mining_pro = response.xpath('//tr[@class="t_empty" and td/a[contains(text(), "Mining Profitability")]]/td[@class="'+self.coin_name+'"]/a/text()').extract()[0]
            item['mining_pro'] = mining_pro
        except IndexError as e:
            print('mining_pro', ' not exist in ', self.coin_name)

        # try:
        #     pass
        # except IndexError as e:
        #     print()

        item['create_time'] = timezone.now()
        print(item)
        yield item
