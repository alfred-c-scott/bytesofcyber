from django.shortcuts import render
from django.views.generic import TemplateView


class PortfolioHomeView(TemplateView):
    template_name = 'portfolio/portfolio_home.html'
