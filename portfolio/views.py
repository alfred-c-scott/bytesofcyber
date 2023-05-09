from django.shortcuts import render
from django.views.generic import TemplateView


class PortfolioHomeView(TemplateView):
    template_name = 'portfolio/portfolio_home.html'


class YoutubeEmbed(TemplateView):
    template_name = 'portfolio/youtube_embed_sample.html'
