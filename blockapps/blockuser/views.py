from django.views.generic import ListView, DetailView, TemplateView
from blockuser.models import QuantPolicy

ITEMS_PER_PAGE = 2

class getQuantListView(ListView):
    queryset = QuantPolicy.objects.order_by('-update_time')
    context_object_name = 'quant_policy_list'
    template_name = 'product/quant_policy_list.html'
    paginate_by = ITEMS_PER_PAGE
    
class getQuantDetailView(DetailView):
    queryset = QuantPolicy.objects.all()
    context_object_name = 'quant_policy_detail'
    template_name = 'product/quant_policy_detail.html'

#@login_required
class ProfileView(TemplateView):
    template_name = 'account/profile.html'
       