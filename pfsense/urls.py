from django.urls import path

from .views import PfSenseInitialSetup, PfSenseHome

app_name = 'pfsense'
urlpatterns = [
    path('', PfSenseHome.as_view(), name='pfsense_home'),
    path('pfsense/initial/', PfSenseInitialSetup.as_view(), name='pfsense_initial_setup')
]
