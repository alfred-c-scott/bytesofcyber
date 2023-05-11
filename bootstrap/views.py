from django.views.generic import TemplateView


class BootStrapHome(TemplateView):
    template_name = 'bootstrap/bootstrap_home.html'


class CardsView(TemplateView):
    template_name = 'bootstrap/bootstrap_cards.html'


class ContentView(TemplateView):
    template_name = 'bootstrap/bootstrap_content.html'
