from django.shortcuts import render
from .models import vw_mapa_integracoes

def home_repositorio(request):
    return render(request, 'repositorio/index.html')

def mapa_integracoes(request):
    mapa = vw_mapa_integracoes.objects.all()

    pn = request.GET.get('id')

    if pn == '' or pn == None:
        pn = None
    else:
        i = int(pn)
        pn = vw_mapa_integracoes.objects.get(id=pn)

    return render(request, 'repositorio/mapa_integracoes.html', {'mapa':mapa, 'pn':pn})
