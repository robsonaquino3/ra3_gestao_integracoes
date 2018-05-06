from django.urls import path
from .views import home, listaCadFleury, examesNaoIntegrados, retornoLaudo

urlpatterns = [
    path('', home, name='home_analises_clinicas'),
    path('lista_cadfleury/', listaCadFleury, name='lista_cadfleury'),
    path('examesnaointegrados/', examesNaoIntegrados, name='examesnaointegrados'),
    path('retornolaudo/', retornoLaudo, name='retornolaudo'),
]
