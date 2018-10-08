from django.conf.urls import include, url
from blockuser.views import getQuantListView,getQuantDetailView,\
                        addDuiqiaoView, manageIndexView, getDuiqiaoDetailView,\
                        getDuiqiaoListView, updateDuiqiaoView, deleteDuiqiaoView                     
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^manage/index/$', login_required(manageIndexView.as_view()), name='manage_index'),
    url(r'^manage/duiqiao/add/$', login_required(addDuiqiaoView.as_view()), name='manage_addduiqiao'),
    url(r'^manage/duiqiao/(?P<pk>[0-9]+)/update/$', login_required(updateDuiqiaoView.as_view()), name='manage_updateduiqiao'),
    url(r'manage/duiqiao/(?P<pk>[0-9]+)/delete/$', login_required(deleteDuiqiaoView.as_view()), name='manage_deleteduiqiao'),
    url(r'^manage/duiqiao/(?P<pk>[0-9]+)/$', login_required(getDuiqiaoDetailView.as_view()), name='manage_getduiqiao'),
    url(r'^manage/duiqiao/list/$', login_required(getDuiqiaoListView.as_view()), name='manage_getduiqiaolist'),
    url(r'^product/quantlist/$', getQuantListView.as_view(), name='product_getquantlist'),
    url(r'^product/quant/(?P<pk>[0-9]+)/$', getQuantDetailView.as_view(), name='product_getquantdetail'),
]
