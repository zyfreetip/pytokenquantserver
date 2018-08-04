from django import forms
from django.forms import ModelForm
from blockuser.models import DuiQiaoPolicy

class DuiqiaoForm(ModelForm):
    class Meta:
        model = DuiQiaoPolicy
        fields = ['user','exchange', 'accesskey', 'secretkey', 'symbol', 'max_buy_price',\
                   'min_sell_price', 'percent_balance', 'start_time', 'end_time']
        
        