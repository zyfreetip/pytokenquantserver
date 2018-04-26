#! /bin/sh
export PATH=$PATH:/usr/local/bin
cd ~/dxc/pyblockchainserver/spiders/deriIndiSpider/deriIndiSpider
nohup scrapy crawl btc_di >> deriIndiSpider.log 2>&1 &
#crontab -e 0 0/10 * * * ? (bin/sh ~/dxc/pyblockchainserver/scripts/btc_deri_spider_run.sh)