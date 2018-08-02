from django.views.generic import ListView
from blockuser.models import QuantPolicy
ITEMS_PER_PAGE = 2

class getQuantListView(ListView):
    queryset = QuantPolicy.objects.order_by('-update_time')
    context_object_name = 'quant_policy_list'
    template_name = 'product/quant_policy_list.html'
    paginate_by = ITEMS_PER_PAGE


    
    