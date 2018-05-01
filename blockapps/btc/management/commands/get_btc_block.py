#encoding=utf8
from django.core.management.base import BaseCommand
from blockserver import settings
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from btc.models import BtcBlockModel
import logging

log_notify = logging.getLogger('block_btc_logs')

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--ip', dest='ip', required=True, help='id address')
        parser.add_argument('--port', dest='port', required=True, help='rpc port')
        parser.add_argument('--user', dest='rpc_user', required=True, help='rpc_user')
        parser.add_argument('--password', dest='rpc_password', required=True, help='rpc_password')

    def handle(self, *args, **options):
        ip = options['ip']
        port = options['port']
        rpc_user = options['rpc_user']
        rpc_password = options['rpc_password']
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpc_user, rpc_password, ip, port))
        blockcount = rpc_connection.getblockcount()
        blocks_flags = {}
        settings.load_config(settings.FLAGS_PATH, blocks_flags)
        start_block_height = blocks_flags['btc']['block_height']
        end_block_height = blockcount
        log_notify.info('btc block height from %s to %s' % (start_block_height, end_block_height))
        for height in range(start_block_height, end_block_height+1):
            block_hash = rpc_connection.getblockhash(height)
            block = rpc_connection.getblock(block_hash)
            BtcBlockModel.objects.get_or_create(
                height=block['height'],
                    defaults={
                    'weight': block['weight'],
                    'version': block['version'],
                    'mrkl_root': block['merkleroot'],
                    'timestamp': block['time'],
                    'size': block['size'],
                    'bits': block['bits'],
                    'nonce': block['nonce'],
                    'hash': block['hash'],
                    'prev_block_hash': block['previousblockhash'] if block['height'] else 0,
                    'next_block_hash': block['nextblockhash'],
                    'difficulty': block['difficulty'],
                    'confirmations': block['confirmations'],
                    },)
        blocks_flags['btc']['block_height'] = end_block_height+1
        settings.update_config(settings.FLAGS_PATH, blocks_flags)
