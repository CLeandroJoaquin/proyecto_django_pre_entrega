from django.shortcuts import render
from Personal.models import Personal, Supervisor, Gerente
# Create your views here.


def listar_personal(request):
    contexto = {
        "Personal": Personal.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Personal/lista_personal.html',
        context=contexto,
    )
    return http_response

