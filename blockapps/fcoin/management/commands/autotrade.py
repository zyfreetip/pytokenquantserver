from django.core.management.base import BaseCommand
from blockuser.duiqiao import duiqiao
import logging

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--exchange', dest='exchange', required=True, \
                help='exchange')
        parser.add_argument('--publickey', dest='publickey', required=True, \
                help='publick key')
        parser.add_argument('--privatekey', dest='privatekey', required=True, \
                help='private key')
        parser.add_argument('--symbol', dest='symbol', required=True, \
                help='trade symbol')
        parser.add_argument('--basevolume', type=float, dest='basevolume', required=True, \
                help='basevolume to use')

    def handle(self, *args, **options):
        import ipdb;ipdb.set_trace()
        exchange = options['exchange']
        symbol = options['symbol']
        publickey = options['publickey']
        privatekey = options['privatekey']
        basevolume = options['basevolume']
        policy = duiqiao(exchange, symbol, publickey, privatekey, basevolume)
        policy.run()