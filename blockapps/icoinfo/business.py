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
        transactions_number_day.update({'cn_name': IcoStatsModel._meta.get_field('transactions_number_day').verbose_name})
        transactions_number_hour.update({'cn_name': IcoStatsModel._meta.get_field('transactions_number_hour').verbose_name})
        total_output_value.update({'cn_name': IcoStatsModel._meta.get_field('total_output_value').verbose_name})
        meidan_transactions_value.update({'cn_name': IcoStatsModel._meta.get_field('meidan_transactions_value').verbose_name})
        block_time.update({'cn_name': IcoStatsModel._meta.get_field('block_time').verbose_name})
        block_count.update({'cn_name': IcoStatsModel._meta.get_field('block_count').verbose_name})
        block_pre_reward.update({'cn_name': IcoStatsModel._meta.get_field('block_pre_reward').verbose_name})
        total_transactions_fees.update({'cn_name': IcoStatsModel._meta.get_field('total_transactions_fees').verbose_name})
        avg_transactions_value.update({'cn_name': IcoStatsModel._meta.get_field('avg_transactions_value').verbose_name})
        difficulty.update({'cn_name': IcoStatsModel._meta.get_field('difficulty').verbose_name})
        hashrate.update({'cn_name': IcoStatsModel._meta.get_field('hashrate').verbose_name})
        blocks_mined_day.update({'cn_name': IcoStatsModel._meta.get_field('blocks_mined_day').verbose_name})
        bitcoins_mined_total.update({'cn_name': IcoStatsModel._meta.get_field('bitcoins_mined_total').verbose_name})
        median_confirmation_time.update({'cn_name': IcoStatsModel._meta.get_field('median_confirmation_time').verbose_name})
        mempool_size.update({'cn_name': IcoStatsModel._meta.get_field('mempool_size').verbose_name})
        current_best_transaction_fees.update({'cn_name': IcoStatsModel._meta.get_field('current_best_transaction_fees').verbose_name})
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
        category.update({'cn_name': IcoBasicInfoModel._meta.get_field('category').verbose_name})
        first_block_time.update({'cn_name': IcoBasicInfoModel._meta.get_field('first_block_time').verbose_name})
        ico_price.update({'cn_name': IcoBasicInfoModel._meta.get_field('ico_price').verbose_name})
        total_volumn.update({'cn_name': IcoBasicInfoModel._meta.get_field('total_volumn').verbose_name})
        maximum_tps.update({'cn_name': IcoBasicInfoModel._meta.get_field('maximum_tps').verbose_name})
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
        wealth_distribution_top10.update({'cn_name': IcoStatsModel._meta.get_field('wealth_distribution_top10').verbose_name})
        wealth_distribution_top100.update({'cn_name': IcoStatsModel._meta.get_field('wealth_distribution_top100').verbose_name})
        wealth_distribution_top1000.update({'cn_name': IcoStatsModel._meta.get_field('wealth_distribution_top1000').verbose_name})
        wealth_distribution_top10000.update({'cn_name': IcoStatsModel._meta.get_field('wealth_distribution_top10000').verbose_name})
        address_richer_than_1usd.update({'cn_name': IcoStatsModel._meta.get_field('address_richer_than_1usd').verbose_name})
        address_richer_than_100usd.update({'cn_name': IcoStatsModel._meta.get_field('address_richer_than_100usd').verbose_name})
        address_richer_than_1000usd.update({'cn_name': IcoStatsModel._meta.get_field('address_richer_than_1000usd').verbose_name})
        address_richer_than_10000usd.update({'cn_name': IcoStatsModel._meta.get_field('address_richer_than_10000usd').verbose_name})
        new_addresses_last24h.update({'cn_name': IcoStatsModel._meta.get_field('new_addresses_last24h').verbose_name})
        active_addresses_last24h.update({'cn_name': IcoStatsModel._meta.get_field('active_addresses_last24h').verbose_name})
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
        mining_pro.update({'cn_name': IcoStatsModel._meta.get_field('mining_pro').verbose_name})
        transactions_fees.update({'cn_name': IcoStatsModel._meta.get_field('transactions_fees').verbose_name})
        cost_per_transaction.update({'cn_name': IcoStatsModel._meta.get_field('cost_per_transaction').verbose_name})
        mining_pro_1thash.update({'cn_name': IcoStatsModel._meta.get_field('mining_pro_1thash').verbose_name})
        per_transactions_volume.update({'cn_name': IcoStatsModel._meta.get_field('per_transactions_volume').verbose_name})
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
        forks = {}
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
                forks.update({ico_name['ico_name']: icoGithub[0].forks})
                issues.update({ico_name['ico_name']: icoGithub[0].issues})
                watchers.update({ico_name['ico_name']: icoGithub[0].watchers})
                codes_this_month.update({ico_name['ico_name']: icoGithub[0].codes_this_month})
                codes_this_week.update({ico_name['ico_name']: icoGithub[0].codes_this_week})
                commits_this_week.update({ico_name['ico_name']: icoGithub[0].commits_this_week})
                commits_this_month.update({ico_name['ico_name']: icoGithub[0].commits_this_month})
        reddit_subscribers.update({'cn_name': IcoSocialMediaModel._meta.get_field('reddit_subscribers').verbose_name})
        twitter_per_day.update({'cn_name': IcoSocialMediaModel._meta.get_field('twitter_per_day').verbose_name})
        release.update({'cn_name': IcoGithubStatsModel._meta.get_field('release').verbose_name})
        stars.update({'cn_name': IcoGithubStatsModel._meta.get_field('stars').verbose_name})
        project_update_time.update({'cn_name': IcoGithubStatsModel._meta.get_field('project_update_time').verbose_name})
        forks.update({'cn_name': IcoGithubStatsModel._meta.get_field('forks').verbose_name})
        issues.update({'cn_name': IcoGithubStatsModel._meta.get_field('issues').verbose_name})
        watchers.update({'cn_name': IcoGithubStatsModel._meta.get_field('watchers').verbose_name})
        codes_this_month.update({'cn_name': IcoGithubStatsModel._meta.get_field('codes_this_month').verbose_name})
        codes_this_week.update({'cn_name': IcoGithubStatsModel._meta.get_field('codes_this_month').verbose_name})
        commits_this_week.update({'cn_name': IcoGithubStatsModel._meta.get_field('commits_this_week').verbose_name})
        commits_this_month.update({'cn_name': IcoGithubStatsModel._meta.get_field('commits_this_month').verbose_name})
        result = [
                {'reddit_subscribers': reddit_subscribers},
                {'twitter_per_day': twitter_per_day},
                {'release': release},
                {'stars': stars},
                {'project_update_time': project_update_time},
                {'forks': forks},
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
                fair_price.update({ico_name['ico_name']: icoExchanges[0].fair_price}) 
                change_24h.update({ico_name['ico_name']: icoExchanges[0].change_24h})
                circulating_supply.update({ico_name['ico_name']: icoExchanges[0].circulating_supply})
                max_supply.update({ico_name['ico_name']: icoExchanges[0].max_supply})
                market_capitalization.update({ico_name['ico_name']: icoExchanges[0].market_capitalization})
                transactions_last_24h.update({ico_name['ico_name']: icoExchanges[0].transactions_last_24h})
                total_trade_volume_24h.update({ico_name['ico_name']: icoExchanges[0].total_trade_volume_24h})
                turnover_rate.update({ico_name['ico_name']: icoExchanges[0].turnover_rate})
        fair_price.update({'cn_name': IcoExchangesStatsModel._meta.get_field('fair_price').verbose_name})
        change_24h.update({'cn_name': IcoExchangesStatsModel._meta.get_field('change_24h').verbose_name})
        circulating_supply.update({'cn_name': IcoExchangesStatsModel._meta.get_field('circulating_supply').verbose_name})
        max_supply.update({'cn_name': IcoExchangesStatsModel._meta.get_field('max_supply').verbose_name})
        market_capitalization.update({'cn_name': IcoExchangesStatsModel._meta.get_field('market_capitalization').verbose_name})
        transactions_last_24h.update({'cn_name': IcoExchangesStatsModel._meta.get_field('transactions_last_24h').verbose_name})
        total_trade_volume_24h.update({'cn_name': IcoExchangesStatsModel._meta.get_field('total_trade_volume_24h').verbose_name})
        turnover_rate.update({'cn_name': IcoExchangesStatsModel._meta.get_field('turnover_rate').verbose_name})
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
