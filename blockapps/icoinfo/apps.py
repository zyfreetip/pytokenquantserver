from icoinfo.models import IcoStatsModel

class IcoInfo(object):
    def init(self):
        pass
    # 获取区块链数据信息
    def getBlockData(self, ctx):
        raise NotImplementedError