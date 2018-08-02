from django.conf.urls import include, url
from blockuser.views import getQuantListView
urlpatterns = [
    #url(r'^login$', loginView.as_view(), name='login'),
    #url(r'^signup$', signupView.as_view(), name='signup'),
    #url(r'^logout$', logoutView.as_view(), name='logout'),
    url(r'^product/getquantlist/$', getQuantListView.as_view(), name='product_getquantlist'),
    #url(r'^addpolicy$', csrf_exempt(addPolicyView.as_view()), name='addpolicy'),
]
