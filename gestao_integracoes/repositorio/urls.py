
from django.urls import path
from .views import home_repositorio, mapa_integracoes

urlpatterns = [
    path('', home_repositorio, name='home_repositorio'),
    path('mapa_integracoes/', mapa_integracoes, name='mapa_integracoes'),

]