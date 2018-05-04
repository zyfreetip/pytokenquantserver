#! /bin/sh
export PATH=$PATH:/usr/local/bin
source ~/dxc/pyblockchainserver/env.sh
cd ~/dxc/pyblockchainserver/spiders/deriIndiSpider
nohup scrapy crawl btc_di >> deriBtcSpider.log &
#crontab -e 0 0/10 * * * ? (bin/sh ~/dxc/pyblockchainserver/scripts/btc_deri_spider_run.sh)