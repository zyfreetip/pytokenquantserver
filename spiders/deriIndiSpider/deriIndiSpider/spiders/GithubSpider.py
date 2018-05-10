from scrapy.spider import Spider
from scrapy import Request

class GithubSpider(Spider):
    name = 'github'

    def start_requests(self):
        url = 'http://v.myhref.com/api/v2/git/datas'
        yield Request(url)

    def parse(self, response):
        content = response.content
        print(content)