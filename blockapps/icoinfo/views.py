#encoding=utf8
from blockdjcom.baseviews import JsonView
from blockdjcom.decorators import unify_params, verify_ctx_required
from blockcomm.net.exceptions import LogicErrorException, Exc_LogicAssertException
from blockdjcom.basebusiness import SSingleton
from acom.utils.designutil import override
import time

class BlockDataView(JsonView):
    @override
    def init(self, ctx):
        pass
    
    @verify_ctx_required
    @unify_params
    def json(self, ctx, request, jrequest, params, *args, **kwargs):
        result = []     
        return result

    def unify_params(self, request, jrequest):
        data = jrequest.get('data',[])
        Exc_LogicAssertException(type(data) is list, 'data should be list,\n%s' \
            % str(jrequest))
        for item in data:
            Exc_LogicAssertException(type(item) is dict, 'data item should be dict,\n%s' \
                % str(jrequest))
        return data