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
    template_name = 'manage/duiqiao/duiqiao_create_form.html'
    model = DuiQiaoPolicy
    fields = ['exchange', 'accesskey', 'secretkey', 'symbol', 'max_buy_price',\
               'min_sell_price', 'percent_balance', 'start_time', 'end_time']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class manageIndexView(TemplateView):
    pass

class getDuiqiaoDetailView(DetailView):
    queryset = DuiQiaoPolicy.objects.all()
    context_object_name = 'duiqiao_detail'
    template_name = 'manage/duiqiao/duiqiao_detail.html'

class getDuiqiaoListView(ListView):
    queryset = DuiQiaoPolicy.objects.order_by('-update_time')
    template_name = 'manage/duiqiao/duiqiao_list.html'
    context_object_name = 'duiqiao_list'
    paginate_by = ITEMS_PER_PAGE
    
    def get_context_data(self, **kwargs):
        return ListView.get_context_data(self, **kwargs)
    