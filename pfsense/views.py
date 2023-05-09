from django.views.generic import TemplateView


class PfSenseHome(TemplateView):
    template_name = 'pfsense/pfsense_home.html'

class PfSenseInitialSetup(TemplateView):
    template_name = 'pfsense/pfsense_initial_setup.html'
