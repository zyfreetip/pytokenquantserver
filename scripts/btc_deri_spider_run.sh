#! /bin/sh
export PATH=$PATH:/usr/local/bin
source /home/ubuntu/dxc/pyblockchainserver/env.sh
cd /home/ubuntu/dxc/pyblockchainserver/spiders/deriIndiSpider
nohup scrapy crawl btc_di >> deriBtcSpider.log &