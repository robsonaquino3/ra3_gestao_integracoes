from django.shortcuts import render
from .models import tb_FleuryLog, tb_fleury_log_nao_integrada, tb_fleury_log_retorno_laudo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'home_analises_clinicas.html')

def listaCadFleury(request):
    data = request.POST.get('dt_evento')

    if data == '' or data == None:
        data = None
        lista = None
        msg = None
        plista = None
    else:
        lista = tb_FleuryLog.objects.filter(dt_evento=data).order_by('ds_estabelecimento')

        paginator = Paginator(lista, 25)  # Show 25 contacts per page

        page = request.GET.get('page')
        plista = paginator.get_page(page)

        try:
            if lista.count() >=1:
                msg = None
            else:
                msg = 'Não há registro para a data informada.'
        except:
            msg = 'Não há registro.'

    return render(request, 'lista_cadfleury.html', {'lista': plista, 'data': data, 'msg': msg})


def examesNaoIntegrados(request):
    data = request.POST.get('dt_evento') or request.GET.get('dt_evento')

    if data == '' or data == None:
        data = None
        lista = None
        msg = None
        plista = None
    else:
        lista = tb_fleury_log_nao_integrada.objects.extra(where=["dt_evento='"+data+"'"])
        paginator = Paginator(lista, 25)  # Show 25 contacts per page

        page = request.GET.get('page')
        plista = paginator.get_page(page)

        try:
            if lista.count() >=1:
                msg = None
            else:
                msg = 'Não há registro para a data informada.'
        except:
            msg = 'Não há registro.'
    return render(request, 'examesnaointegrados.html', {'lista': plista, 'data': data, 'msg': msg})

def retornoLaudo(request):
    data = request.POST.get('dt_evento') or request.GET.get('dt_evento')

    if data == '' or data == None:
        data = None
        lista = None
        msg = None
        plista = None
    else:
        lista = tb_fleury_log_retorno_laudo.objects.extra(where=["dt_evento='"+data+"'"]).order_by('ds_estabelecimento')
        paginator = Paginator(lista, 25)  # Show 25 contacts per page

        page = request.GET.get('page')
        plista = paginator.get_page(page)

        try:
            if lista.count() >=1:
                msg = None
            else:
                msg = 'Não há registro para a data informada.'
        except:
            msg = 'Não há registro.'
    return render(request, 'retornolaudoexames.html', {'lista': plista, 'data': data, 'msg': msg})