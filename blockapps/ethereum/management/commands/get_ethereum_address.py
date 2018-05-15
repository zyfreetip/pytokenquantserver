# encoding=utf8
from django.core.management.base import BaseCommand
from ethereum.models import EthereumAddressModel, EthereumBlockModel, EthereumTransactionModel, EthereumTransactionReceiptModel
from web3 import Web3, HTTPProvider
from logging import info as loginfo
import ipdb
from multiprocessing import Pool


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
        # 暂时去除增量更新功能
        pools = Pool(16)
        ethereumblockmodels = []
        if ethereumblockmodels:
            print('更新数据')
            start_block_number = ethereumblockmodels[0].number
            for number in range(start_block_number, block_number+1):
                block = w3.eth.getBlock(number, True)
                # self.get_info(block, w3)
                pools.apply_async(func=self.get_info, args=(block, w3))

        else:
            print('第一次获取数据')
            for number in range(1, block_number):
                block = w3.eth.getBlock(number, True)
                # self.get_info(block, w3)
                pools.apply_async(func=self.get_info, args=(block, w3))
        pools.close()
        pools.join()

    def get_info(self, block, w3):
        transactions = self.get_transactions_from_block(block)
        print("transactions count:", len(transactions), ' in block ', block['number'])
        for transaction in transactions:
            double_address = self.get_address_from_transaction(transaction)
            print('transaction: ', transaction['hash'].hex())
            if double_address[0]:
                balance = w3.eth.getBalance(double_address[0])
                self.handle_by_address(double_address[0], transaction, 'received', balance)
            if double_address[1]:
                balance = w3.eth.getBalance(double_address[1])
                self.handle_by_address(double_address[1], transaction, 'sent', balance)

    def get_transactions_from_block(self, block):
        transactions_ = block['transactions']
        return transactions_

    def get_address_from_transaction(self, transaction):
        # from代表sent，to代表received
        from_address = transaction['from']
        to_address = transaction['to']
        return to_address, from_address

    def handle_by_address(self, address, transaction, opstr, balance):
        # 总接受量，总支出量可以通过transaction表查询
        # 或者遍历的方式
        received_or_send = ''
        if opstr == 'received':
            received_or_send = 'received'
        else:
            received_or_send = 'sent'
        model_qs = EthereumAddressModel.objects.filter(address=address)
        if len(model_qs) != 0:
            data_qs = model_qs[0]
            print('data_qs', data_qs)
            received_or_sent_str = (data_qs.received, data_qs.sent)[opstr == 'received']
            if received_or_sent_str == '':
                received_or_sent_str = '0'
            tx_count = data_qs.tx_count+1
            EthereumAddressModel.objects.update_or_create(
                address=address,
                defaults={
                    received_or_send: transaction['value']+int(received_or_sent_str),
                    'tx_count': tx_count,
                    'balance': balance,
                }
            )
        else:
            print('address第一次出现在数据库')
            EthereumAddressModel.objects.update_or_create(
                address=address,
                defaults={
                    received_or_send: transaction['value'],
                    'tx_count': 1,
                    'balance': balance
                }
            )
