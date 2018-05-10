from scrapy.spider import Spider
from scrapy import Request
import re
from deriIndiSpider.items import IcoMeiaItem

class MediaSpider(Spider):
    name = 'media'

    def __init__(self):
        pass

    def handle_string(self, content, rtype=0):
        number_list = re.findall(r'\d+\.?\d*', content)
        target = ''
        for single in number_list:
            target += single
        print("targt>>>>>>", )
        if rtype == 0:
            target = int(target)
        elif rtype == 1:
            target = float(target)
        return target

    def start_requests(self):
        url = 'https://bitinfocharts.com'
        yield Request(url)

    def parse(self, response):
        # reddit订阅数
        try:
            reddits = response.xpath('//tr[@id="t_reddit"]/td/text()').extract()[1:9]
            reddits = list(map(lambda x:self.handle_string(x), reddits))
            twitters = response.xpath('//tr[@id="t_twitter"]/td/text()').extract()[0:8]
            twitters = list(map(lambda x: self.handle_string(x), twitters))
            names =  response.xpath('//tr[@class="t_coin"]/td/a/text()').extract()[:8]
            names =list(map(lambda x:x.strip(), names))
            for i in range(8):
                item = IcoMeiaItem()
                item['ico_name'] = names[i]
                item['reddit_subscribers'] = reddits[i]
                item['twitter_per_day'] = twitters[i]
                print("item is :", item)
                yield item

        except IndexError as e:
            print('ico_name', 'not exist in ', self.coin_name)
        # 每日推文数
