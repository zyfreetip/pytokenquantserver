from scrapy.spiders import Spider
from scrapy import Request
from deriIndiSpider.items import IcoInfoSpiderItem

class ICOBenchSpider(Spider):
    name = 'icobench'

    def start_requests(self):
        url = 'https://icobench.com/icos'
        yield Request(url, callback=self.get_onepage_urls)

    def parse(self, response):
        item = IcoInfoSpiderItem()
        project_name = response.xpath('//h1/text()').extract()[0]
        name = project_name[:project_name.find('(')].strip()
        item['ico_name'] = name

        token_name =  response.xpath('//div[@class="data_row"][1]/div[@class="col_2"][2]/b/text()').extract()[0]
        item['token'] = token_name

        price = response.xpath('//div[@class="data_row"][3]/div[@class="col_2"][2]/b/text()').extract()[0]
        item['price'] = price

        country =  response.xpath('//div[@class="data_row"][10]/div[@class="col_2"][2]/b/a/text()').extract()[0]
        item['country'] = country

        # 国家中文名字
        #todo

        # token发行总量
        tokens = response.xpath
        item['tokens'] = tokens
        yield item
        #




    # 获取到单页上所有的项目url
    def get_onepage_urls(self, response):
        urls = response.xpath("//td[@class='ico_data']//a[@class='name']/@href").extract()
        urls = list(map(lambda x: 'https://icobench.com'+x, urls))
        for url in urls:
            print('urls:', url)
            yield Request(url)
        # 一页上面的ico项目提取完成，进行下一页的数据处理
        next_url = response.xpath("//a[@class='next']/@href").extract()
        if next_url:
            yield Request('https://icobench.com'+next_url, callback=self.get_onepage_urls)
        else:
            return

