from django.urls import path
from .views import BootStrapHome, CardsView, ContentView

app_name = 'bootstrap'
urlpatterns = [
    path('', BootStrapHome.as_view(), name='bootstrap_home'),
    path('cards/', CardsView.as_view(), name='bootstrap_cards'),
    path('content/', ContentView.as_view(), name='bootstrap_content')
]
