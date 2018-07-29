from django.conf.urls import include, url
from .views import blockchainView
urlpatterns = [
    #url(r'^login$', loginView.as_view(), name='login'),
    #url(r'^signup$', signupView.as_view(), name='signup'),
    #url(r'^logout$', logoutView.as_view(), name='logout'),
    url(r'^product/blockchain_list$', blockchainView.as_view(), name='blockchain_list'),
    #url(r'^addpolicy$', csrf_exempt(addPolicyView.as_view()), name='addpolicy'),
]
