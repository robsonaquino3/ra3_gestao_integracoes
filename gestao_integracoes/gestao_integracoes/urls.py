
from django.contrib import admin
from django.urls import path, include
from gestao_integracoes.views import pagina_principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analises_clinicas/', include('analises_clinicas.urls')),
    path('repositorio/', include('repositorio.urls')),
    path('', pagina_principal, name='pagina_principal'),


]
