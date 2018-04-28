# encoding=utf8
from django.core.management.base import BaseCommand
from ethereum.models import EthereumAddressModel, EthereumBlockModel, EthereumTransactionModel, EthereumTransactionReceiptModel
from web3 import Web3, HTTPProvider
from logging import info as loginfo
import ipdb


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--ip', dest='ip', required=True, help='ip address')
        parser.add_argument('--port', dest='port', required=True, help='RPC port')

    def handle(self, *args, **options):
        ip = options['ip']
        port = options['port']
        print("ip:", ip, "port", port)
        w3 = Web3(HTTPProvider(ip + ':' + port))
        block_number = w3.eth.blockNumber
        ethereumblockmodels = EthereumBlockModel.objects.all().order_by('-number')
        if ethereumblockmodels:
            print('更新数据')
            start_block_number = ethereumblockmodels[0].number
            for number in range(start_block_number, block_number+1):
                block = w3.eth.getBlock(number, True)
                self.get_info(block)

        else:
            print('第一次获取数据')
            for number in range(1, block_number):
                block = w3.eth.getBlock(number, True)
                self.get_info(block)

    def get_info(self, block):
        transactions = self.get_transactions_from_block(block)
        print("transactions:", transactions)
        for transaction in transactions:
            double_address = self.get_address_from_transacton(transaction)
            self.handle_by_address(double_address[0], transaction)
            self.handle_by_address(double_address[1], transaction)

    def get_transactions_from_block(self, block):
        transactions_ = block['transactions']
        return transactions_

    def get_address_from_transaction(self, transaction):
        from_address = transaction['from']
        to_address = transaction['from']
        return from_address, to_address

    def handle_by_address(self, address, transaction):
        # 总接受量，总支出量可以通过transaction表查询
        # 或者遍历的方式
        model_qs = EthereumAddressModel.objects.filter(address=address)
        if len(model_qs) != 0:
            received_str = model_qs[0]['received']
            EthereumAddressModel.objects.update_or_create(
                address=address,
                defaults={
                    'received': int(transaction['value']+int(received_str))
                }
            )
        else:
            EthereumAddressModel.objects.update_or_create(
                address=address,
                defaults={
                    'received': str(transaction['value'])
                }
            )
