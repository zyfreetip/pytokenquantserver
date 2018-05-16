from scrapy.spiders import Spider
from scrapy import Request
from deriIndiSpider.items import IcoInfoSpiderItem

class ICOBenchSpider(Spider):
    name = 'icobench'

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
        }
        self.urls = []
    def start_requests(self):
        url = 'https://icobench.com/icos'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
        }
        yield Request(url, callback=self.get_onepage_urls, headers=header)

    def parse(self, response):
        print("current url:", response.url)
        item = IcoInfoSpiderItem()
        project_name = response.xpath('//h1/text()').extract()[0]
        name = project_name[:project_name.find('(')].strip()
        item['ico_name'] = name

        try:
            token_name_xpath = '//div[@class="data_row"]/div[contains(text(), "Token")]/following-sibling::*/b/text()'
            token_name =  response.xpath(token_name_xpath).extract()[0]
            item['token'] = token_name
        except IndexError as e:
            print("token name not exist or xpath error in ", response.url)
        try:
            price_xpath = '//div[@class="data_row"]/div[contains(text(), "Price")]/following-sibling::*/b/text()'
            price = response.xpath(price_xpath).extract()[0]
            item['price'] = price
        except IndexError as e:
            print("price not exist or xpath error in ", response.url)

        try:
            country_xpath = '//div[@class="data_row"]/div[contains(text(), "Country")]/following-sibling::*/b/a/text()'
            country =  response.xpath(country_xpath).extract()[0]
            item['country'] = country
        except IndexError as e:
            print("country not exist or xpath error in ", response.url)

        # 国家中文名字
        #todo

        # token总量
        try:
            tokens = response.xpath("//div[@class='label' and text()='Tokens for sale']/following-sibling::div/text()").extract()[0]
            item['tokens'] = tokens
        except IndexError as e:
            print("token name not exist or xpath error in ", response.url)

        try:
            token_type_xpath = '//div[@class="label" and contains(text(), "Type")]/following-sibling::div/text()'
            token_type = response.xpath(token_type_xpath).extract()[0]
            item['token_type'] = token_type
        except IndexError as e:
            print("token type not exist or xpath error in ", response.url)

        #hardcap
        try:
            hardcap_xpath = '//div[@class="data_row"]/div[contains(text(), "Hard cap")]/following-sibling::*/b/text()'
            hardcap = response.xpath(hardcap_xpath).extract()[0]
            item['hardcap'] = hardcap
        except IndexError as  e:
            print("hardcap not exist or xpath error in ", response.url)

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

        try:

            time_xpath = '//small[contains(text(),"20") and contains(text(), "-")]/text()'
            time_string = response.xpath(time_xpath).extract()[0]

            ico_start = time_string.split(' - ')[0]
            ico_end = time_string.split(' - ')[1]
            item['ico_start'] = ico_start
            item['ico_end'] = ico_end
        except IndexError as e:
            print('time not exist or xpath error in ', response.url)

        try:
            distributed_xpath = '//div[@class="label" and contains(text(), "Distributed")]/following-sibling::div/text()'
            distributed = response.xpath(distributed_xpath).extract()[0]
            item['distributed'] = distributed
        except IndexError:
            print("distributed 不存在:", response.url)


        try:
            tagline_xpath = '//div[@class="name"]/h2/text()'
            tagline = response.xpath(tagline_xpath).extract()[0]
            item['tagline'] = tagline
        except IndexError as e:
            print("tagline not exist or xpath error in ", response.url)

        yield item
        #



    # 获取到单页上所有的项目url
    def get_onepage_urls(self, response):
        urls = response.xpath("//td[@class='ico_data']//a[@class='name']/@href").extract()
        urls = list(map(lambda x: 'https://icobench.com'+ x + '/financial', urls))
        for url in urls:
            print('urls:', url)
            # yield Request(url, headers=self.header)
            self.urls.append(url)
        # 一页上面的ico项目提取完成，进行下一页的数据处理
        next_url = response.xpath("//a[@class='next']/@href").extract()
        if next_url:
            print('Page Size: '+next_url[0])
            yield Request('https://icobench.com'+next_url[0], callback=self.get_onepage_urls, headers=self.header)
        else:
            print("final urls: ", self.urls)
            for url in self.urls:
                yield Request(url, headers=self.header)

