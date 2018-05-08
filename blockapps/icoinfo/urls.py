from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from .views import BlockDataView 
urlpatterns = [
    url(r'^blockData$', csrf_exempt(BlockDataView.as_view()), name='icoinfo_blockdata'),
]