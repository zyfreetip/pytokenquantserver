class DbRouter:
    DB_MAP = {  'btc':
                {
                 'btc_block': ('btc_block_ro', 'btc_block'),
                 'btc_address': ('btc_address_ro', 'btc_address'),
                 'btc_transaction':('btc_transaction_ro', 'btc_transaction'),
                 'btc_output_transaction':('btc_output_transaction_ro', 'btc_output_transaction'),
                 'btc_input_transaction':('btc_input_transaction_ro', 'btc_input_transaction'),
                 'btc_stats':('btc_stats_ro', 'btc_stats'),
                 'btc_index':('btc_index_ro', 'btc_index'),
                },
                'ethereum':
                {
                 'ethereum_block': ('ethereum_block_ro', 'ethereum_block'),
                 'ethereum_address': ('ethereum_address_ro', 'ethereum_address'),
                 'ethereum_transaction':('ethereum_transaction_ro', 'ethereum_transaction'),
                 'ethereum_transaction_receipt':('ethereum_transaction_receipt_ro', 'ethereum_transaction_receipt'),
                 'ethereum_stats':('ethereum_stats_ro', 'ethereum_stats'),
                 'ethereum_index':('ethereum_index_ro', 'ethereum_index'),
                },
                'huobi':
                {'huobi_btc_stats': ('huobi_btc_stats_ro', 'huobi_btc_stats'),
                 'huobi_ethereum_stats': ('huobi_ethereum_stats_ro', 'huobi_ethereum_stats'),
                },
				'icoinfo':
				{
				'ico_data': ('ico_data_ro', 'ico_data'),
                'ico_social_medial': ('ico_social_medial_ro', 'ico_social_medial'),
                'ico_github_stats': ('ico_github_stats_ro', 'ico_github_stats'),
                'ico_exchanges_stats': ('ico_exchanges_stats_ro', 'ico_exchanges_stats'),
                'ico_stats': ('ico_stats_ro', 'ico_stats'),
                'ico_basic_info': ('ico_basic_info_ro', 'ico_basic_info'),
				}
            }

    def _getRoDB(self, mapinfo, model=None):
        kwargs = {}
        if model.__name__.startswith('Db'):
            kwargs['dbnum'] = model.__name__[2:4]
        if kwargs:
            dbalias = mapinfo[0] % kwargs
        else:
            dbalias = mapinfo[0]
        return dbalias

    def _getRwDB(self, mapinfo, model=None):
        kwargs = {}
        if model.__name__.startswith('Db'):
            kwargs['dbnum'] = model.__name__[2:4]
        if kwargs:
            dbalias = mapinfo[1] % kwargs
        else:
            dbalias = mapinfo[1]
        return dbalias

    def db_for_read(self, model, **hints):
        app_db_map = DbRouter.DB_MAP.get(model._meta.app_label, {})
        mapinfo = app_db_map.get(model._meta.db_table, None)
        if not mapinfo: return None
        return self._getRoDB(mapinfo, model)

    def db_for_write(self, model, **hints):
        app_db_map = DbRouter.DB_MAP.get(model._meta.app_label, {})
        mapinfo = app_db_map.get(model._meta.db_table, None)
        if not mapinfo: return None
        return self._getRwDB(mapinfo, model)

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label not in DbRouter.DB_MAP:
            return None
        app_db_map = DbRouter.DB_MAP[app_label]
        for model_name0, dbs in app_db_map.items():
            if type(dbs) in (tuple, list):
# rwdb
                if dbs[1] == db:
                    return True
            else:
                for modelcls, mapinfo in dbs.items():
                    if mapinfo[1] == db:
                        return True
        return None
# init mult db map
for suffix in range(1,10):
    DbRouter.DB_MAP['btc']['btc_address%03d' % suffix] = ('btc_address_ro', 'btc_address')
