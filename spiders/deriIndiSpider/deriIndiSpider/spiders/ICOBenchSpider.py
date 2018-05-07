from scrapy.spiders import Spider
from scrapy import Request
from deriIndiSpider.items import IcoInfoSpiderItem

class ICOBenchSpider(Spider):
    name = 'icobench'

    def start_requests(self):
        url = 'https://icobench.com/icos'
        yield Request(url, callback=self.get_onepage_urls)

    def parse(self, response):
        print("current url:", response.url)
        item = IcoInfoSpiderItem()
        project_name = response.xpath('//h1/text()').extract()[0]
        name = project_name[:project_name.find('(')].strip()
        item['ico_name'] = name

        token_name_xpath = '//div[@class="data_row"]/div[contains(text(), "Token")]/following-sibling::*/b/text()'
        token_name =  response.xpath(token_name_xpath).extract()[0]
        item['token'] = token_name

        price_xpath = '//div[@class="data_row"]/div[contains(text(), "Price")]/following-sibling::*/b/text()'
        price = response.xpath(price_xpath).extract()[0]
        item['price'] = price

        country_xpath = '//div[@class="data_row"]/div[contains(text(), "Country")]/following-sibling::*/b/a/text()'
        country =  response.xpath(country_xpath).extract()[0]
        item['country'] = country

        # 国家中文名字
        #todo

        # token总量
        tokens = response.xpath
        item['tokens'] = tokens

        token_type_xpath = '//div[@class="label" and contains(text(), "Type")]/following-sibling::div/text()'
        token_type = response.xpath(token_type_xpath).extract()[0]
        item['token_type'] = token_type

        #hardcap
        hardcap_xpath = '//div[@class="data_row"]/div[contains(text(), "Hard cap")]/following-sibling::*/b/text()'
        hardcap = response.xpath(hardcap_xpath).extract()[0]
        item['hardcap'] = hardcap

        # soft cap
        softcap_xpath = '//div[@class="data_row"]/div[contains(text(), "Soft cap")]/following-sibling::*/b/text()'
        try:
            softcap = response.xpath(softcap_xpath).extract()[0]
            item['softcap'] = softcap
        except IndexError:
            print("softcap 不存在 in", response.url)

        # raised
        raised_xpath = '//div[@class="data_row"]/div[contains(text(), "Raised")]/following-sibling::*/b/text()'
        try:
            raised = response.xpath(raised_xpath).extract()[0]
            item['raised'] = raised
        except Exception as e:
            # raise没有则不存
            print("raised 不存在 in :", response.url)


        time_xpath = '//small[contains(text(),"20") and contains(text(), "-")]/text()'
        time_string = response.xpath(time_xpath).extract()[0]

        ico_start = time_string.split(' - ')[0]
        ico_end = time_string.split(' - ')[1]
        item['ico_start'] = ico_start
        item['ico_end'] = ico_end

        distributed_xpath = '//div[@class="label" and contains(text(), "Distributed")]/following-sibling::div/text()'
        distributed = response.xpath(distributed_xpath).extract()[0]
        item['distributed'] = distributed

        tagline_xpath = '//div[@class="name"]/h2/text()'
        tagline = response.xpath(tagline_xpath).extract()[0]
        item['tagline'] = tagline

        yield item
        #




    # 获取到单页上所有的项目url
    def get_onepage_urls(self, response):
        urls = response.xpath("//td[@class='ico_data']//a[@class='name']/@href").extract()
        urls = list(map(lambda x: 'https://icobench.com'+ x + '/financial', urls))
        for url in urls:
            print('urls:', url)
            yield Request(url)
        # 一页上面的ico项目提取完成，进行下一页的数据处理
        next_url = response.xpath("//a[@class='next']/@href").extract()
        if next_url:
            yield Request('https://icobench.com'+next_url[0], callback=self.get_onepage_urls)
        else:
            return

