from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from .views import getBlockDataView 
urlpatterns = [
    url(r'^getblockdata$', csrf_exempt(getBlockDataView.as_view()), name='icoinfo_getblockdata'),
]