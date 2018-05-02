#! /bin/sh
export PATH=$PATH:/usr/local/bin
cd ~/dxc/pyblockchainserver/spiders/deriIndiSpider/deriIndiSpider
nohup scrapy crawl eth_di >> deriEthSpider.log 2>&1 &
#crontab -e 0 0/10 * * * ? (bin/sh ~/dxc/pyblockchainserver/scripts/eth_deri_spider_run.sh)