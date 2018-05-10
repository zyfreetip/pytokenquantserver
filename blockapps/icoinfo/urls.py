from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from .views import getBlockDataView, getBlockBasicInfoView,  getBlockAddrInfoView, \
                getBlockMineInfoView, getBlockMediaInfoView, getBlockMarketCapView

urlpatterns = [
    url(r'^getblockdata$', csrf_exempt(getBlockDataView.as_view()), name='icoinfo_getblockdata'),
    url(r'^getblockbasicinfo$', csrf_exempt(getBlockBasicInfoView.as_view()), name='icoinfo_getblockbasicinfo'),
    url(r'^getblockaddrinfo$', csrf_exempt(getBlockAddrInfoView.as_view()), name='icoinfo_getblockaddrinfo'),
    url(r'^getblockmineinfo$', csrf_exempt(getBlockMineInfoView.as_view()), name='icoinfo_getblockmineinfo'),
    url(r'^getblockmediainfo$', csrf_exempt(getBlockMediaInfoView.as_view()), name='icoinfo_getblockmediainfo'),
    url(r'^getblockmarketcap$', csrf_exempt(getBlockMarketCapView.as_view()), name='icoinfo_getblockmarketcap'),
]