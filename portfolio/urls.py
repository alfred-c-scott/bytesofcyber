from django.urls import path
from .views import PortfolioHomeView, YoutubeEmbed


app_name = 'portfolio'
urlpatterns = [
    path('', PortfolioHomeView.as_view(), name='home'),
    path('youtube/', YoutubeEmbed.as_view(), name='youtube_embed')
]
