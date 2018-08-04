from django.conf.urls import include, url
from blockuser.views import getQuantListView,getQuantDetailView, ProfileView,\
                        addDuiqiaoView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^accounts/profile/$', login_required(ProfileView.as_view()), name='account_profile'),
    #url(r'^signup$', signupView.as_view(), name='signup'),
    #url(r'^logout$', logoutView.as_view(), name='logout'),
    url(r'^manage/addduiqiao/$', login_required(addDuiqiaoView.as_view()), name='manage_addduiqiao'),
    url(r'^product/getquantlist/$', getQuantListView.as_view(), name='product_getquantlist'),
    url(r'^product/getquant/(?P<pk>[0-9]+)/$', getQuantDetailView.as_view(), name='product_getquantdetail'),
    #url(r'^addpolicy$', csrf_exempt(addPolicyView.as_view()), name='addpolicy'),
]
