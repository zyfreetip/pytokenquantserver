from scrapy.spider import Spider
from scrapy import Request
import json
from deriIndiSpider.items import IcoGithubItem

class GithubSpider(Spider):
    name = 'github'

    def __init__(self):
        self.mapper = {
            'BTC':'Bitcoin',
            'ETH':'Ethereum',
            'XRP':'Ripple',
            'BCH':'Bitcoin Cash',
            'LTC': 'Litecoin',
            'DASH': 'Dash',
            'XMR': 'Monero',
            'ETC': 'Ethereum Classic',
            'EOS': 'EOS',
            'ADA': 'ADA',
            'NEO': 'NEO'
        }

    def start_requests(self):
        url = 'http://v.myhref.com/api/v2/git/datas'
        yield Request(url)

    def parse(self, response):
        content = response.body_as_unicode()[5:-1]
        jsonContent = json.loads(content)["infos"]
        for one in jsonContent:
            # print(item)
            if one["code"] in ['BTC', 'ETH', 'XRP', 'BCH', 'LTC', 'XMR', 'DASH', 'ETC', 'EOS', 'ADA', 'NEO']:
                print(one["code"])
                item = IcoGithubItem()
                ico_name = one["code"]
                stars = one["watchersCount"]
                commits_this_month = one["commitCountAMonth"]
                codes_this_month = one["addCodesCountAMonth"]
                forks = one["forksCount"]
                issues = one["openIssuesCount"]
                codes_this_week = one["addCodesCountAWeek"]
                commits_this_week = one["commitCountAWeek"]
                item["ico_name"] = self.mapper[ico_name]
                item["stars"] = stars
                item["commits_this_month"] = commits_this_month
                item["codes_this_month"] = codes_this_month
                item["forks"] = forks
                item["issues"] = issues
                item["codes_this_week"] = codes_this_week
                item["commits_this_week"] = commits_this_week
                yield item


            else:
                print(one["code"], "not store")
        # print(content)