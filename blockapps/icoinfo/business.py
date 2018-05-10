from icoinfo.models import IcoStatsModel, IcoSocialMediaModel, IcoGithubStatsModel, IcoExchangesStatsModel,\
                            IcoBasicInfoModel

class icoInfo(object):

    def init(self):
        pass
    # 获取区块链数据信息
    def getBlockData(self, ctx):
        result = []
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
                transactions_number_hour.update({ico_name['ico_name']: icoStats[0].transactions_number_hour})
                total_output_value.update({ico_name['ico_name']: icoStats[0].total_output_value})
                meidan_transactions_value.update({ico_name['ico_name']: icoStats[0].meidan_transactions_value})
                block_time.update({ico_name['ico_name']: icoStats[0].block_time})
                block_count.update({ico_name['ico_name']: icoStats[0].block_count})
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
        result = [ {'transactions_number_day': transactions_number_day},
                   { 'transactions_number_hour': transactions_number_hour},
                   {'total_output_value': total_output_value},
                   { 'meidan_transactions_value': meidan_transactions_value},
                   { 'block_time': block_time},
                   { 'block_count': block_count},
                   { 'block_pre_reward': block_pre_reward},
                   {'total_transactions_fees': total_transactions_fees},
                   { 'avg_transactions_value': avg_transactions_value},
                   {'difficulty': difficulty},
                   { 'hashrate': hashrate},
                   { 'blocks_mined_day': blocks_mined_day},
                   {'bitcoins_mined_total': bitcoins_mined_total},
                   {'median_confirmation_time': median_confirmation_time},
                   {'mempool_size': mempool_size},
                   { 'current_best_transaction_fees': current_best_transaction_fees}
                 ] 
        return result
    
    # 获取区块链数据信息
    def getBlockBasicInfo(self, ctx):
        result = []
        category = {}
        first_block_time = {}
        ico_price = {}
        total_volumn = {}
        maximum_tps = {}
        ico_names = IcoStatsModel.objects.values('ico_name').distinct()
        for ico_name in ico_names:
            icoStats = IcoBasicInfoModel.objects.filter(ico_name=ico_name['ico_name']).order_by('-create_time')
            if icoStats: 
                category.update({ico_name['ico_name']: icoStats[0].category})
                first_block_time.update({ico_name['ico_name']: icoStats[0].first_block_time})
                ico_price.update({ico_name['ico_name']: icoStats[0].ico_price})
                total_volumn.update({ico_name['ico_name']: icoStats[0].total_volumn})
                maximum_tps.update({ico_name['ico_name']: icoStats[0].maximum_tps})
        result = [ {'category': category},
                  {'first_block_time': first_block_time},
                  {'ico_price': ico_price},
                  {'total_volumn': total_volumn},
                  {'maximum_tps': maximum_tps}
                ]
        return result 
        
    def getBlockAddrInfo(self, ctx):
        result = []
        wealth_distribution_top10 = {}
        wealth_distribution_top100 = {}
        wealth_distribution_top1000 = {}
        wealth_distribution_top10000 = {}
        address_richer_than_1usd = {}
        address_richer_than_100usd = {}
        address_richer_than_1000usd = {}
        address_richer_than_10000usd = {}
        new_addresses_last24h = {}
        active_addresses_last24h = {}
        ico_names = IcoStatsModel.objects.values('ico_name').distinct()
        for ico_name in ico_names:
            icoStats = IcoStatsModel.objects.filter(ico_name=ico_name['ico_name']).order_by('-create_time')
            if icoStats: 
                wealth_distribution_top10.update({ico_name['ico_name']: icoStats[0].wealth_distribution_top10})
                wealth_distribution_top100.update({ico_name['ico_name']: icoStats[0].wealth_distribution_top100})
                wealth_distribution_top1000.update({ico_name['ico_name']: icoStats[0].wealth_distribution_top1000})
                wealth_distribution_top10000.update({ico_name['ico_name']: icoStats[0].wealth_distribution_top10000})
                address_richer_than_1usd.update({ico_name['ico_name']: icoStats[0].address_richer_than_1usd})
                address_richer_than_100usd.update({ico_name['ico_name']: icoStats[0].address_richer_than_100usd})
                address_richer_than_1000usd.update({ico_name['ico_name']: icoStats[0].address_richer_than_1000usd})
                address_richer_than_10000usd.update({ico_name['ico_name']: icoStats[0].address_richer_than_10000usd})
                new_addresses_last24h.update({ico_name['ico_name']: icoStats[0].new_addresses_last24h})
                active_addresses_last24h.update({ico_name['ico_name']: icoStats[0].active_addresses_last24h})
        result = [ {'wealth_distribution_top10': wealth_distribution_top10},
                   {'wealth_distribution_top100': wealth_distribution_top100},
                   {'wealth_distribution_top1000': wealth_distribution_top1000},
                   { 'wealth_distribution_top10000': wealth_distribution_top10000},
                   { 'address_richer_than_1usd': address_richer_than_1usd},
                   { 'address_richer_than_100usd': address_richer_than_100usd},
                   { 'address_richer_than_1000usd': address_richer_than_1000usd},
                   {'address_richer_than_10000usd': address_richer_than_10000usd},
                   { 'new_addresses_last24h': new_addresses_last24h},
                   {'active_addresses_last24h': active_addresses_last24h},
                 ] 
        return result
    
    def getBlockMineInfo(self, ctx):
        result = []
        mining_pro = {}
        transactions_fees = {}
        cost_per_transaction = {}
        mining_pro_1thash = {}
        per_transactions_volume = {}
        ico_names = IcoStatsModel.objects.values('ico_name').distinct()
        for ico_name in ico_names:
            icoStats = IcoStatsModel.objects.filter(ico_name=ico_name['ico_name']).order_by('-create_time')
            if icoStats:
                mining_pro.update({ico_name['ico_name']: icoStats[0].mining_pro})
                transactions_fees.update({ico_name['ico_name']: icoStats[0].transactions_fees})
                cost_per_transaction.update({ico_name['ico_name']: icoStats[0].cost_per_transaction})
                mining_pro_1thash.update({ico_name['ico_name']: icoStats[0].mining_pro_1thash})
                per_transactions_volume.update({ico_name['ico_name']: icoStats[0].per_transactions_volume})
        result = [ { 'mining_pro': mining_pro},
                   { 'transactions_fees': transactions_fees},
                   {'cost_per_transaction': cost_per_transaction},
                   {'mining_pro_1thash': mining_pro_1thash},
                   {'per_transactions_volume': per_transactions_volume}
                 ] 
        return result

    def getBlockMediaInfo(self, ctx):
        result = []
        reddit_subscribers = {}
        twitter_per_day = {}
        release = {}
        stars = {}
        project_update_time = {}
        branches = {}
        issues = {}
        watchers = {}
        codes_this_month = {}
        codes_this_week = {}
        commits_this_month = {}
        commits_this_week = {}
        ico_names = IcoStatsModel.objects.values('ico_name').distinct()
        for ico_name in ico_names:
            icoMedias = IcoSocialMediaModel.objects.filter(ico_name=ico_name['ico_name']).order_by('-create_time')
            if icoMedias:
                reddit_subscribers.update({ico_name['ico_name']: icoMedias[0].reddit_subscribers}) 
                twitter_per_day.update({ico_name['ico_name']: icoMedias[0].twitter_per_day}) 
            icoGithub = IcoGithubStatsModel.objects.filter(ico_name=ico_name['ico_name']).order_by('-create_time')
            if icoGithub:
                release.update({ico_name['ico_name']: icoGithub[0].release}) 
                stars.update({ico_name['ico_name']: icoGithub[0].stars})
                project_update_time.update({ico_name['ico_name']: icoGithub[0].project_update_time})
                branches.update({ico_name['ico_name']: icoGithub[0].branches})
                issues.update({ico_name['ico_name']: icoGithub[0].issues})
                watchers.update({ico_name['ico_name']: icoGithub[0].watchers})
                codes_this_month.update({ico_name['ico_name']: icoGithub[0].codes_this_month})
                codes_this_week.update({ico_name['ico_name']: icoGithub[0].codes_this_week})
                commits_this_week.update({ico_name['ico_name']: icoGithub[0].commits_this_week})
                commits_this_month.update({ico_name['ico_name']: icoGithub[0].commits_this_month})
        result = [
                {'reddit_subscribers': reddit_subscribers},
                {'twitter_per_day': twitter_per_day},
                {'release': release},
                {'stars': stars},
                {'project_update_time': project_update_time},
                {'branches': branches},
                {'issues': issues},
                {'watchers': watchers},
                {'codes_this_month': codes_this_month},
                {'codes_this_week': codes_this_week},
                {'commits_this_month': commits_this_month},
                {'commits_this_week': commits_this_week},
            ]
        return result
    
    def getBlockMarketcap(self, ctx):
        result = []
        fair_price = {}
        change_24h = {}
        circulating_supply = {}
        max_supply = {}
        market_capitalization = {}
        transactions_last_24h = {}
        total_trade_volume_24h = {}
        turnover_rate = {}
        ico_names = IcoStatsModel.objects.values('ico_name').distinct()
        for ico_name in ico_names:
            icoExchanges = IcoExchangesStatsModel.objects.filter(ico_name=ico_name['ico_name']).order_by('-create_time')
            if icoExchanges:
                fair_price.update({ico_name['ico_name']: icoExchanges[0].release}) 
                change_24h.update({ico_name['ico_name']: icoExchanges[0].change_24h})
                circulating_supply.update({ico_name['ico_name']: icoExchanges[0].circulating_supply})
                max_supply.update({ico_name['ico_name']: icoExchanges[0].max_supply})
                market_capitalization.update({ico_name['ico_name']: icoExchanges[0].market_capitalization})
                transactions_last_24h.update({ico_name['ico_name']: icoExchanges[0].transactions_last_24h})
                total_trade_volume_24h.update({ico_name['ico_name']: icoExchanges[0].total_trade_volume_24h})
                turnover_rate.update({ico_name['ico_name']: icoExchanges[0].turnover_rate})
        result = [
                {'fair_price': fair_price},
                {'change_24h': change_24h},
                {'circulating_supply': circulating_supply},
                {'max_supply': max_supply},
                {'market_capitalization': market_capitalization},
                {'transactions_last_24h': transactions_last_24h},
                {'total_trade_volume_24h': total_trade_volume_24h},
                {'turnover_rate': turnover_rate},
            ]
        return result