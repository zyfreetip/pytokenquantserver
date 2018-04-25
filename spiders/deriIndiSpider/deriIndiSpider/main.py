import sys
import os
from scrapy.cmdline import execute

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute("scrapy crawl btc_di -o result.csv".split())
execute(["scrapy", "crawl", "btc_di"])