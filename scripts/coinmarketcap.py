#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 19:38:43 2018

@author: shijunjing
"""

import requests
import json
import time

import pymysql.cursors


connection = pymysql.connect(host='uat-mysql-cluster.cluster-co6y7bekwid1.ap-northeast-1.rds.amazonaws.com',
                             user='blockchainsh',
                             password='Blockchain002!$#',
                             db='icoinfo',
                             cursorclass=pymysql.cursors.DictCursor)

coins=['bitcoin','ethereum','ripple','bitcoin-cash','litecoin','cardano','neo','dash','monero','ethereum-classic']
while True:
    for i in coins:
        try:
            coin_raw=requests.get('https://api.coinmarketcap.com/v1/ticker/{0}/'.format(i))
            chart=json.loads(coin_raw.text)
            ico_name=chart[0]['name']
            token=chart[0]['symbol']
            fair_price=chart[0]['price_usd']
            change_24h=chart[0]['percent_change_24h']
            circulating_supply=chart[0]['available_supply']
            max_supply=chart[0]['max_supply']
            market_capitalization=chart[0]['market_cap_usd']
            transactions_last_24h=chart[0]['24h_volume_usd']
            total_trade_volume_24h=float(transactions_last_24h)/float(fair_price)
            turnover_rate=total_trade_volume_24h/float(circulating_supply)
            print(ico_name,token,fair_price,change_24h,circulating_supply,max_supply,market_capitalization,transactions_last_24h,total_trade_volume_24h,turnover_rate)
            connection.cursor().execute('insert into ico_exchanges_stats (ico_name,token,fair_price,change_24h,circulating_supply,max_supply,market_capitalization,transactions_last_24h,total_trade_volume_24h,turnover_rate,create_time) values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}",now())'.format(ico_name,token,fair_price,change_24h,circulating_supply,max_supply,market_capitalization,transactions_last_24h,total_trade_volume_24h,turnover_rate))
            connection.commit()     
        except:
            continue
    time.sleep(120)
connection.close()