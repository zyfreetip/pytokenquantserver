from django.core import serializers
from .basebusiness import baseFcoin
import json
import logging
import time

auto_trade_log = logging.getLogger('fcoin_auto_trade_log') 
class Fcoin(baseFcoin):
    MARKET_DEPTH_LEVEL = 'L20'
    FCOIN_REWARD_REFER = 0.00
    # 查找需要卖的订单
    def get_orders_to_sell(self, symbol):
        result =[]
        response = self.get_orders_list(symbol, 'filled', '', '', 100)
        if response['status'] != 0:
            return
        orders = response['data']
        if not orders:
            return result
        # 目前只检查最近的2笔订单
        if orders[0]['side'] == 'buy' and orders[0]['state'] in ('filled',\
                'partial_filled', 'partial_canceled'):
                result.append({'symbol': orders[0]['symbol'],
                                'buy_price': orders[0]['price'],
                                'filled_amount': orders[0]['filled_amount'],
                                'buy_order_id': orders[0]['id']
                                })
        return result
    
    # 卖出订单
    def do_sell_policy(self, symbol, buy_price, remain_amount):
        while True:
            # 查询盘口卖单数量
            level = self.MARKET_DEPTH_LEVEL
            symbol=symbol
            response = self.get_market_depth(symbol, level)
            time.sleep(1)
            if response['status'] != 0:
                continue
            depth = response['data']
            buy_1_price = depth['bids'][0]
            buy_1_volume = depth['bids'][1]
            # 目前fcoin盈利规则
            reward_percent = (0.01 + 0.01)*self.FCOIN_REWARD_REFER
            buy_price = buy_price
            buy_amount = remain_amount
            if buy_price < buy_1_price * (1 + reward_percent):
                # 立刻卖出
                symbol=symbol
                side='sell'
                order_type='limit'
                sell_price=buy_1_price
                if buy_amount <= buy_1_volume:
                    sell_amount = buy_amount
                else:
                    sell_amount = buy_1_volume
                response = self.create_order(symbol, side, order_type, str(sell_price), str(sell_amount)) 

                if response['status'] != 0:
                    continue
                sell_order_id = response['data']
                remain_amount = self.check_order_filled_or_not(sell_order_id, sell_amount)
                if remain_amount != 0:
                    self.cancel_order_until_success(sell_order_id)
                    continue
                break
    # 查询订单是否成交
    def check_order_filled_or_not(self, order_id, amount):
        while True:
            remain_amount = 0
            time.sleep(3)
            response = self.get_order_by_id(order_id)
            if response['status'] != 0:
                auto_trade_log.info('get  order %s  failed: status(%d)' % \
                            (order_id, response['status']))           
                continue 
            if response['data']['state'] == 'filled':
                auto_trade_log.info('order_id(%s) filled: filled_amount:%s' %\
                (order_id, response['data']['filled_amount']))
                return 0
            elif response['data']['state'] == 'partial_filled':
                remain_amount = amount - response['data']['filled_amount']
                auto_trade_log.info('order_id(%s) partial_filled: filled_amount:%s remain_amount:%s ' %\
                (order_id, response['data']['filled_amount'], remain_amount))
                return remain_amount
            else:
                auto_trade_log.info('order_id(%s) partial_filled: filled_amount:%s remain_amount:%s ' %\
                (order_id, response['data']['filled_amount'], amount))
                return amount
        
    # 撤销订单
    def cancel_order_until_success(self, order_id):
        while True:
            time.sleep(2)
            response = self.cancel_order(order_id)
            # 取消失败已经成交的订单 
            if response['status'] == 3008:
                auto_trade_log.info('cancel order %s  failed: status(%d)' % \
                                    (order_id, response['status']))           
                break
            # 查询订单是否取消
            time.sleep(2)
            response = self.get_order_by_id(order_id)
            if response['status'] != 0:
                auto_trade_log.info('get order %s  failed: status(%d)' % \
                        (order_id, response['status']))           
                continue
            data = response['data']
            if data['state'] not in ('partial_canceled', 'canceled'):
                continue
            return
    # 账户各币种余额
    def get_coin_balances(self):
        response = self.get_balance()
        if response['status'] != 0:
            auto_trade_log.info('get balance failed: status(%d)' % \
                    (response['status']))           
            return
        rsp_balances = response['data']
        balances = {}
        for balance in rsp_balances:
            balances.update({balance['currency']:{'available':balance['available'],
                                                  'frozen': balance['frozen'],
                                                  'balance': balance['balance']}
                                                  })  
        return balances

    # 下买单
    def do_buy_policy(self, symbol, percent):
        while True:
            # policy1: 低买高卖策略: buy_price < sell_price * (1 + 0.00004)
            # step1: 获取ticker数据
            time.sleep(5)
            response  = self.get_market_ticker(symbol)
            # 获取最新成交价和成交量，计算合理买入价格和买入量。
            if response['status'] != 0 :
                auto_trade_log.info('get %s ticker failed: status(%d)' % \
                        (symbol, response['status']))           
                continue
            ticker = response['data']['ticker']
            deal_latest_price = ticker[0]
            deal_latest_amount = ticker[1]
            deal_buy_max_price = ticker[2]
            deal_buy_max__amount = ticker[3]
            deal_sell_min_price = ticker[4]
            deal_sell_min_amount = ticker[5]
            deal_before_24h_price = ticker[6]
            deal_in_24h_max_price = ticker[7]
            deal_in_24h_min_price = ticker[8]
            deal_in_24h_base_volume = ticker[9]
            deal_in_24h_quote_volume = ticker[10]
           
            # step2: 获取最新成交记录
            limit = 1000
            before = 0 
            response = self.get_market_orders(symbol, limit, before)
            if response['status'] != 0 :
                auto_trade_log.info('get %s %d %d order failed: status(%d)' % \
                        (symbol,limit, before, response['status']))           
                continue
            deal_records = response['data']
            deal_buy_records = []
            deal_sell_records = []
            for deal in deal_records:
                if deal['side'] == 'buy':
                    deal_buy_records.append(deal)
                elif deal['side'] == 'sell':
                    deal_sell_records.append(deal)
            deal_record_buy_1_price = deal_buy_records[0]['price']
            deal_record_buy_1_volume = deal_buy_records[0]['amount']
            deal_record_buy_2_price = deal_buy_records[1]['price']
            deal_record_buy_2_volume = deal_buy_records[1]['amount']
            deal_record_buy_3_price = deal_buy_records[2]['price']
            deal_record_buy_3_volume = deal_buy_records[2]['amount']
            
            deal_record_sell_1_price = deal_sell_records[0]['price']
            deal_record_sell_1_volume = deal_sell_records[0]['amount']
            deal_record_sell_2_price = deal_sell_records[1]['price']
            deal_record_sell_2_volume = deal_sell_records[1]['amount']
            deal_record_sell_3_price = deal_sell_records[2]['price']
            deal_record_sell_3_volume = deal_sell_records[2]['amount']
            
            # 根据成交历史记录计算均衡价格？

            # step3: 获取盘口深度
            level = 'L20'
            response = self.get_market_depth(symbol, level)
            if response['status'] != 0:
                auto_trade_log.info('get %s %s depth failed: status(%d)' % \
                        (symbol, level, response['status']))           
                continue
            depth = response['data']
            buy_1_price = depth['bids'][0]
            buy_1_volume = depth['bids'][1]
            buy_2_price = depth['bids'][2]
            buy_2_volume = depth['bids'][3]
            buy_3_price = depth['bids'][4]
            buy_3_volume = depth['bids'][5]

            sell_1_price = depth['asks'][0]
            sell_1_volume = depth['asks'][1]
            sell_2_price = depth['asks'][2]
            sell_2_volume = depth['asks'][3]
            sell_3_price = depth['asks'][4]
            sell_3_volume = depth['asks'][5]

            # step2: 下买单
            # 下买单的买入价格如何选取？
            buy_price = buy_1_price 

            # 查询账户余额
            balances = self.get_coin_balances()
            # 下买单
            symbol = symbol
            side = 'buy'
            order_type = 'limit'
            buy_price = buy_price
            # 这里可以根据symbol来判断买入的基准货币是哪个
            if symbol[-4:] == 'usdt': 
                available_balance = float(balances['usdt']['available'])
            elif symbol[-3:] == 'eth':
                available_balance = float(balances['eth']['available'])
            elif symbol[-3:] == 'btc':
                available_balance = float(balances['btc']['available'])
            elif symbol[-2:] == 'ft':
                available_balance = float(balances['ft']['available'])
            buy_amount = round(available_balance/buy_price*percent, 4)
            response = self.create_order(symbol, side, order_type, \
                    str(buy_price), str(buy_amount))
            if response['status'] != 0:
                auto_trade_log.info('buy price:%f amount:%f failed: status(%d)'\
                        %(buy_price, buy_amount, response['status']))           
                continue
            buy_order_id = response['data']
            remain_amount = self.check_order_filled_or_not(buy_order_id, buy_amount)
            if remain_amount == buy_amount:
                self.cancel_order_until_success(buy_order_id)
                continue
            buy_amount = buy_amount - remain_amount
            return buy_price, buy_amount
