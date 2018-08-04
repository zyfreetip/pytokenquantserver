from django.views.generic import ListView, DetailView, TemplateView,\
                            CreateView
from blockuser.models import QuantPolicy, DuiQiaoPolicy


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

class addDuiqiaoView(CreateView):
    template_name = 'manage/duiqiao_create_form.html'
    model = DuiQiaoPolicy
    fields = ['user','exchange', 'accesskey', 'secretkey', 'symbol', 'max_buy_price',\
               'min_sell_price', 'percent_balance', 'start_time', 'end_time']