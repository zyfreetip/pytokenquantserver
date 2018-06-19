#encoding=utf8
from blockdjcom.baseviews import JsonView
from blockdjcom.decorators import unify_params, verify_ctx_required
from icoinfo.business import icoInfo
from acom.utils.designutil import override

class getBlockDataView(JsonView):
    @override
    def init(self, ctx):
        self.icoInfo = icoInfo()
    
    @verify_ctx_required
    @unify_params
    def json(self, ctx, request, jrequest, params, *args, **kwargs):   
        result = []
        data = params
        if not data:
            result.extend(self.doGet(ctx))
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data',[])
        return data

    # input { }
    def doGet(self, ctx):
        result = self.icoInfo.getBlockData(ctx)
        return result

class getBlockBasicInfoView(JsonView):
    @override
    def init(self, ctx):
        self.icoInfo = icoInfo()
    
    @verify_ctx_required
    @unify_params
    def json(self, ctx, request, jrequest, params, *args, **kwargs):   
        result = []
        data = params
        if not data:
            result.extend(self.doGet(ctx))
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data',[])
        return data

    # input { }
    def doGet(self, ctx):
        result = self.icoInfo.getBlockBasicInfo(ctx)
        return result

class getBlockAddrInfoView(JsonView):
    @override
    def init(self, ctx):
        self.icoInfo = icoInfo()
    
    @verify_ctx_required
    @unify_params
    def json(self, ctx, request, jrequest, params, *args, **kwargs):   
        result = []
        data = params
        if not data:
            result.extend(self.doGet(ctx))
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data',[])
        return data

    # input { }
    def doGet(self, ctx):
        result = self.icoInfo.getBlockAddrInfo(ctx)
        return result

class getBlockMineInfoView(JsonView):
    @override
    def init(self, ctx):
        self.icoInfo = icoInfo()
    
    @verify_ctx_required
    @unify_params
    def json(self, ctx, request, jrequest, params, *args, **kwargs):   
        result = []
        data = params
        if not data:
            result.extend(self.doGet(ctx))
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data',[])
        return data

    # input { }
    def doGet(self, ctx):
        result = self.icoInfo.getBlockMineInfo(ctx)
        return result
    
class getBlockMediaInfoView(JsonView):
    @override
    def init(self, ctx):
        self.icoInfo = icoInfo()
    
    @verify_ctx_required
    @unify_params
    def json(self, ctx, request, jrequest, params, *args, **kwargs):   
        result = []
        data = params
        if not data:
            result.extend(self.doGet(ctx))
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data',[])
        return data

    # input { }
    def doGet(self, ctx):
        result = self.icoInfo.getBlockMediaInfo(ctx)
        return result

class getBlockMarketCapView(JsonView):
    @override
    def init(self, ctx):
        self.icoInfo = icoInfo()
    
    @verify_ctx_required
    @unify_params
    def json(self, ctx, request, jrequest, params, *args, **kwargs):   
        result = []
        data = params
        if not data:
            result.extend(self.doGet(ctx))
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data',[])
        return data

    # input { }
    def doGet(self, ctx):
        result = self.icoInfo.getBlockMarketcap(ctx)
        return result

class getIcoinfoView(JsonView):
    @override
    def init(self, ctx):
        self.icoInfo = icoInfo()

    @verify_ctx_required
    @unify_params
    def json(self, ctx, request, jrequest, params, *args, **kwargs):
        result = []
        data = params
        if not data:
            result.extend(self.doGet(ctx))
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data', [])
        return data

    def doGet(self, ctx):
        result = self.icoInfo.getIcoinfo(ctx)
        return result