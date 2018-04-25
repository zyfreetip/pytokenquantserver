#encoding=utf8
from django.core.management.base import BaseCommand
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

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
        print(blockcount)
        commands = [ [ "getblockhash", height] for height in range(100) ]
        block_hashes = rpc_connection.batch_(commands)
        blocks = rpc_connection.batch_([ [ "getblock", h ] for h in block_hashes ])
        block_times = [ block["time"] for block in blocks ]
        print(block_times)
        
        