'''
Created on 2018年8月16日

@author: qiaoxiaofeng
'''
from quantpolicy.business import quantpolicy

class duiqiao(quantpolicy):
    
    def __init__(self, exchange, symbol, accesskey, secretkey,\
                 max_buy_price, min_sell_price, percent_balance):
         super().__init__(exchange, symbol, accesskey, secretkey)
         self.max_buy_price = max_buy_price
         self.min_sell_price = min_sell_price
         self.percent_balance = percent_balance
    
    def run(self):
         