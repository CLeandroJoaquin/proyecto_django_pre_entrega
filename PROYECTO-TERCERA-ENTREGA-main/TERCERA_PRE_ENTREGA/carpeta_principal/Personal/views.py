from django.shortcuts import render
from Personal.models import Personal, Ventas, Inventario
from django.http import HttpResponse
# Create your views here.


def lista_personal(request):
    contexto = {
        "personal": Personal.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Personal/lista_personal.html',
        context=contexto,
    )
    return http_response

