from icoinfo.models import IcoStatsModel

class icoInfo(object):

    def init(self):
        pass
    # 获取区块链数据信息
    def getBlockData(self, ctx):
        transactions_number_day = {}
        transactions_number_hour = {}
        total_output_value = {}
        meidan_transactions_value = {}
        block_time = {}
        block_count= {} 
        block_pre_reward =  {}
        total_transactions_fees = {}
        avg_transactions_value = {}
        difficulty = {}
        hashrate = {}
        blocks_mined_day = {}
        bitcoins_mined_total = {}
        median_confirmation_time = {}
        mempool_size = {}
        current_best_transaction_fees = {}
        ico_names = IcoStatsModel.objects.values('ico_name').distinct()
        for ico_name in ico_names:
            icoStats = IcoStatsModel.objects.filter(ico_name=ico_name['ico_name']).order_by('-create_time')
            if icoStats: 
                transactions_number_day.update({ico_name['ico_name']: icoStats[0].transactions_number_day})
                transactions_number_hour.updaet({ico_name['ico_name']: icoStats[0].transactions_number_hour})
                total_output_value.update.update({ico_name['ico_name']: icoStats[0].total_output_value})
                meidan_transactions_value.update({ico_name['ico_name']: icoStats[0].meidan_transactions_value})
                block_time.update({ico_name['ico_name']: icoStats[0].block_time})
                block_count.updaet({ico_name['ico_name']: icoStats[0].block_count})
                block_pre_reward.update({ico_name['ico_name']: icoStats[0].block_pre_reward})
                total_transactions_fees.update({ico_name['ico_name']: icoStats[0].total_transactions_fees})
                avg_transactions_value.update({ico_name['ico_name']: icoStats[0].avg_transactions_value})
                difficulty.update({ico_name['ico_name']: icoStats[0].difficulty})
                hashrate.update({ico_name['ico_name']: icoStats[0].hashrate}) 
                blocks_mined_day.update({ico_name['ico_name']: icoStats[0].blocks_mined_day}) 
                bitcoins_mined_total.update({ico_name['ico_name']: icoStats[0].bitcoins_mined_total})
                median_confirmation_time.update({ico_name['ico_name']: icoStats[0].median_confirmation_time})
                mempool_size.update({ico_name['ico_name']: icoStats[0].mempool_size})
                current_best_transaction_fees.update({ico_name['ico_name']: icoStats[0].current_best_transaction_fees})
        result = { 'transactions_number_day': transactions_number_day,
                    'transactions_number_hour': transactions_number_hour,
                    'total_output_value': total_output_value,
                    'meidan_transactions_value': meidan_transactions_value,
                    'block_time': block_time,
                    'block_count': block_count,
                    'block_pre_reward': block_pre_reward,
                    'total_transactions_fees': total_transactions_fees,
                    'avg_transactions_value': avg_transactions_value,
                    'difficulty': difficulty,
                    'hashrate': hashrate,
                    'blocks_mined_day': blocks_mined_day,
                    'bitcoins_mined_total': bitcoins_mined_total,
                    'median_confirmation_time': median_confirmation_time,
                    'mempool_size': mempool_size,
                    'current_best_transaction_fees': current_best_transaction_fees
                    } 
        return result