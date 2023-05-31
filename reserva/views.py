from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

# Create your views here.
def index(request):
    return HttpResponse('Marcos Fábio Carneiro e Silva')


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes.html", context={"clientes": clientes})