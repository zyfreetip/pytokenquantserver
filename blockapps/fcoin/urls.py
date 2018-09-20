from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from .views import getBlockDataView, getBlockBasicInfoView,  getBlockAddrInfoView, \
                getBlockMineInfoView, getBlockMediaInfoView, getBlockMarketCapView, getIcoinfoView

urlpatterns = [
]