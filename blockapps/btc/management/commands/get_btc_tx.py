#encoding=utf8
from django.core.management.base import BaseCommand
from blockserver import settings
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from btc.models import BtcInputTransactionModel
from btc.models import BtcOutputTransactionModel
from btc.models import BtcAddressModel
from btc.models import BtcTransactionModel
import logging

log_notify = logging.getLogger('block_btc_tx_logs') 
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
        start_block_height = blocks_flags['btc']['tx_block_height'] if blocks_flags['btc']['tx_block_height'] else 1
        end_block_height = blockcount
        log_notify.info('btc tx block height from %s to %s' % (start_block_height, end_block_height))
        for height in range(start_block_height, end_block_height+1):
            block_hash = rpc_connection.getblockhash(height)
            block = rpc_connection.getblock(block_hash)
            commands = [ ['getrawtransaction', tx, True ] for tx in block['tx'] ]
            transactions = rpc_connection.batch_(commands)
            for tx in transactions:
                inputs_value = 0
                is_coinbase = 0
                for vin in tx['vin']:
                    if 'coinbase' in vin.keys():
                        is_coinbase = 1
                    else:
                        trx = rpc_connection.getrawtransaction(vin['txid'],True)
                        for vout in trx['vout']:
                            if vin['vout'] == vout['n']:
                                txhash = tx['hash']
                                prev_value = vout['value']*pow(10,8)
                                prev_position = vout['n']
                                script_asm = vout['scriptPubKey']['asm']
                                script_hex = vout['scriptPubKey']['hex']
                                sequence = vin['sequence']
                                prev_tx_hash = trx['hash']
                                for address in vout['scriptPubKey']['addresses']:
                                    prev_address = address
                                    btcaddressmodel, created = BtcAddressModel.objects.get_or_create(address=address, defaults={
                                            'tx_count': 1,
                                            'sent': prev_value,
                                            'balance': 0})
                                    if btcaddressmodel:
                                        btcaddressmodel.tx_count +=1
                                        btcaddressmodel.sent += prev_value
                                        btcaddressmodel.balance = btcaddressmodel.received - btcaddressmodel.sent if btcaddressmodel.received - btcaddressmodel.sent > 0 else 0
                                        btcaddressmodel.save()
                                    BtcInputTransactionModel.objects.create(txhash=txhash,
                                                                            prev_value=prev_value,
                                                                            prev_position=prev_position,
                                                                            script_hex=script_hex,
                                                                            script_asm=script_asm,
                                                                            sequence=sequence,
                                                                            prev_tx_hash=prev_tx_hash,
                                                                            prev_address=prev_address,
                                                                            )
                                inputs_value += prev_value
                outputs_value = 0
                for vout in tx['vout']:
                    txhash = tx['hash']
                    value = vout['value']*pow(10,8)
                    try:
                        for address in vout['scriptPubKey']['addresses']:
                            btcaddressmodel, created = BtcAddressModel.objects.get_or_create(address=address, defaults={
                                    'tx_count': 1,
                                    'received': value})
                            if btcaddressmodel:
                                btcaddressmodel.tx_count += 1
                                btcaddressmodel.received += value
                                btcaddressmodel.balance = btcaddressmodel.received - btcaddressmodel.sent if btcaddressmodel.received - btcaddressmodel.sent > 0 else 0
                                btcaddressmodel.save()
                            BtcOutputTransactionModel.objects.create(txhash=txhash,
                                                                     value=value,
                                                                     address=address)
                            outputs_value += value
                    except KeyError as e:
                        continue
                version = tx['version']
                size = tx['size']
                locktime = tx['locktime']
                blocktime = tx['blocktime']
                confirmations = tx['confirmations']
                BtcTransactionModel.objects.get_or_create(txhash=tx['txid'],
                                                          defaults={
                                                          'block_height': height,
                                                          'block_time': blocktime,
                                                          'inputs_count': len(vin),
                                                          'outputs_count': len(vout),
                                                          'is_coinbase': is_coinbase,
                                                          'version': version,
                                                          'size': size,
                                                          'lock_time': locktime,
                                                          'outputs_value':outputs_value,
                                                          'inputs_value': inputs_value,
                                                          'confirmations': confirmations,
                                                          })
            log_notify.info('btc tx block height(%s) success' % (height))
        blocks_flags['btc']['tx_block_height'] = end_block_height+1
        settings.update_config(settings.FLAGS_PATH, blocks_flags)
