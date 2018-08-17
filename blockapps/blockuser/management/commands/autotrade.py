from django.core.management.base import BaseCommand
from fcoin.models import MarketTradeOrderModel
from fcoin.business import Fcoin
import logging

auto_trade_log = logging.getLogger('fcoin_auto_trade_log') 
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--publickey', dest='publickey', required=True, \
                help='publick key')
        parser.add_argument('--privatekey', dest='privatekey', required=True, \
                help='private key')
        parser.add_argument('--symbol', dest='symbol', required=True, \
                help='trade symbol')
        parser.add_argument('--percent', type=float, dest='percent', required=True, \
                help='quote coin balance percent to use')

    def handle(self, *args, **options):
        symbol = options['symbol']
        publickey = options['publickey']
        privatekey = options['privatekey']
        percent = options['percent']
        fcoin=Fcoin(publickey,privatekey)
        # 先检查订单列表哪些成交订单没有全部卖出
        ordersToSell = fcoin.get_orders_to_sell(symbol)
        # 否则就先卖出该笔订单
        for orderToSell in ordersToSell:
            pass
            #fcoin.do_sell_policy(orderToSell['symbol'], float(orderToSell['buy_price']), float(orderToSell['filled_amount']))
        # policy1: 低买高卖策略: buy_price < sell_price * (1 + 0.00004)
        buy_price, buy_amount = fcoin.do_buy_policy(symbol, percent)
        fcoin.do_sell_policy(symbol, buy_price, buy_amount)
