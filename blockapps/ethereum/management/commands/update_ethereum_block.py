#encoding=utf8
from django.core.management.base import BaseCommand
from ethereum.models import EthereumBlockModel, EthereumTransactionModel
from web3 import Web3, HTTPProvider


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--ip', dest='ip', required=True, help='ip address')
        parser.add_argument('--port', dest='port', required=True, help='RPC port')

    def handle(self, *args, **options):
        ip = options['ip']
        port = options['port']
        w3 = Web3(HTTPProvider(ip+':'+port))
        ethereumblockmodel = EthereumBlockModel.objects.all().order_by('-height')[0]
        startblockheight = ethereumblockmodel.height
        blocknumber = w3.eth.blockNumber
        for height in range(startblockheight+1, blocknumber+1):
            block = w3.eth.getBlock(height, True)
            # block data
            EthereumBlockModel.objects.get_or_create(
                number=block['number'],
                defaults={
                    'hash': block['hash'],
                    'parent_hash': block['parentHash'],
                    'nonce': block['nonce'],
                    'transaction_root': block['transactionRoot'],
                    'state_root': block['stateRoot'],
                    'receipts_root': block['receiptRoot'],
                    'miner': block['miner'],
                    'difficulty': block['difficulty'],
                    'total_difficulty': block['totalDifficulty'],
                    'extra_data': block['extraData'],
                    'size': block['size'],
                    'gas_limit': block['gasLimit'],
                    'gas_used': block['gasUsed'],
                    'timestamp': block['timestamp'],
                }
            )

            # transactions
            transactions = block['transactions']
            for transaction in transactions:
                EthereumTransactionModel.objects.get_or_create(
                    txhash=transaction['hash'],
                    defaults = {
                        'nonce': transaction['nonce'],
                        'block_hash': transaction['blockHash'],
                        'block_number': transaction['blockNumber'],
                        'txindex': transaction['transactionIndex'],
                        'from_address': transaction['from'],
                        'to_address': transaction['to'],
                        'value': transaction['value'],
                        'gas_price': transaction['gasPrice'],
                        'gas': transaction['gas'],
                        'input_data': transaction['input'],

                    }
                )
