#encoding=utf8
from django.core.management.base import BaseCommand
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from btc.models import BtcInputTransactionModel
from btc.models import BtcOutputTransactionModel
from btc.models import BtcAddressModel
from btc.models import BtcTransactionModel

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
        #rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpc_user, rpc_password, ip, port))])
        BtcAddressModels = BtcAddressModel.objects.all()
        for AddressModel in BtcAddressModels:
            received = 0
            sent = 0
            balance = 0
            tx_count = 0
            unconfirmed_tx_count = 0
            unconfirmed_rx_count = 0
            unconfirmed_sent = 0
            unspent_tx_count = 0
            address = AddressModel.address
            btcInputTxs = BtcInputTransactionModel.objects.filter(prev_address=address)
            for inputTx in btcInputTxs:
                tx_count += 1
                sent += inputTx.prev_value
            btcOutputTxs = BtcOutputTransactionModel.objects.filter(address=address)
            for outputTx in btcOutputTxs:
                tx_count += 1
                received += outputTx.value
            balance = received - sent
            BtcAddressModel.objects.update(address=address,
                                         received=received,
                                         sent=sent,
                                         balance=balance,
                                         tx_count=tx_count,
                                         )