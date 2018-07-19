from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from .views import loginView,signupView, logoutView, dashboardView,\
			addPolicyView

urlpatterns = [
    url(r'^login$', csrf_exempt(loginView.as_view()), name='login'),
    url(r'^signup$', csrf_exempt(signupView.as_view()), name='signup'),
    url(r'^logout$', csrf_exempt(logoutView.as_view()), name='logout'),
    url(r'^dashboard$', csrf_exempt(dashboardView.as_view()), name='dashboard'),
    url(r'^addpolicy$', csrf_exempt(addPolicyView.as_view()), name='addpolicy'),
]
