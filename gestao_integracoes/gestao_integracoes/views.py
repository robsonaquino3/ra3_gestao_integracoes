from django.shortcuts import render

def pagina_principal(request):
    return render(request, 'teste.html')

