# encoding=utf8
from django.core.management.base import BaseCommand
from ethereum.models import EthereumBlockModel, EthereumTransactionModel, EthereumTransactionReceiptModel
from web3 import Web3, HTTPProvider
from logging import info as loginfo

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--ip', dest='ip', required=True, help='ip address')
        parser.add_argument('--port', dest='port', required=True, help='RPC port')

    def handle(self, *args, **options):
        ip = options['ip']
        port = options['port']
        loginfo('ip:'+str(ip))
        loginfo('port:'+str(port))
        w3 = Web3(HTTPProvider(ip+':'+port))
        # ethereumblockmodel = EthereumBlockModel.objects.all().order_by('-number')[0]
        # startblockheight = ethereumblockmodel.height
        blocknumber = w3.eth.blockNumber
        for height in range(1, blocknumber+1):
            block = w3.eth.getBlock(height, True)
            # block data
            EthereumBlockModel.objects.get_or_create(
                number=block['number'],
                defaults={
                    'hash': block['hash'],
                    'parent_hash': block['parentHash'],
                    'nonce': block['nonce'],
                    'transactions_root': block['transactionsRoot'],
                    'state_root': block['stateRoot'],
                    'receipts_root': block['receiptsRoot'],
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
                self.store_transaction(transaction)
                self.store_transaction_receipt(w3, transaction['hash'])

    # transaction
    def store_transaction_receipt(self, web3, txhash):
        receipt = web3.eth.getTransactionReceipt(txhash)
        EthereumTransactionReceiptModel.objects.get_or_create(
            txhash=receipt['transactionHash'],
            defaults={
                'txhash': receipt['transactionHash'],
                'txindex': receipt['transactionIndex'],
                'block_hash': receipt['blockHash'],
                'block_number': receipt['blockNumber'],
                'total_gas': receipt['cumulativeGasUsed'],
                'gas_used': receipt['gas_used'],
                'contract_address': receipt['contractAddress'],
                'root': receipt['root'],
                'status': receipt['status'],
            }
        )

    def store_transaction(self, transaction):
        loginfo("transaction:")
        loginfo(transaction)
        EthereumTransactionModel.objects.get_or_create(
            txhash=transaction['hash'],
            defaults={
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
