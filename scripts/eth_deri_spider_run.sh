#! /bin/sh
export PATH=$PATH:/usr/local/bin
source ~/dxc/pyblockchainserver/env.sh
cd ~/dxc/pyblockchainserver/spiders/deriIndiSpider
nohup scrapy crawl eth_di >> deriEthSpider.log 2>&1 &
#crontab -e 0/15 * * * * ? (bin/sh ~/dxc/pyblockchainserver/scripts/eth_deri_spider_run.sh)
