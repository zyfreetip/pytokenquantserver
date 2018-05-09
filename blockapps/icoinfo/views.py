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
            result.append(self.doGet(ctx))
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data',[])
        return data

    # input { }
    def doGet(self, ctx):
        result = self.icoInfo.getBlockData(ctx)
        return result
