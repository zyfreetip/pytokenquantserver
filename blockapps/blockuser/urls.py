from django.conf.urls import include, url
from blockuser.views import getQuantListView,getQuantDetailView, ProfileView,\
                        addDuiqiaoView, manageIndexView, getDuiqiaoDetailView,\
                        getDuiqiaoListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^accounts/profile/$', login_required(ProfileView.as_view()), name='account_profile'),
    #url(r'^signup$', signupView.as_view(), name='signup'),
    #url(r'^logout$', logoutView.as_view(), name='logout'),
    url(r'^manage/index/$', login_required(manageIndexView.as_view()), name='manage_index'),
    url(r'^manage/duiqiao/add/$', login_required(addDuiqiaoView.as_view()), name='manage_addduiqiao'),
    url(r'^manage/duiqiao/(?P<pk>[0-9]+)/$', login_required(getDuiqiaoDetailView.as_view()), name='manage_getduiqiao'),
    url(r'^manage/duiqiaolist/$', login_required(getDuiqiaoListView.as_view()), name='manage_getduiqiaolist'),
    url(r'^product/quantlist/$', getQuantListView.as_view(), name='product_getquantlist'),
    url(r'^product/quant/(?P<pk>[0-9]+)/$', getQuantDetailView.as_view(), name='product_getquantdetail'),
    #url(r'^addpolicy$', csrf_exempt(addPolicyView.as_view()), name='addpolicy'),
]
