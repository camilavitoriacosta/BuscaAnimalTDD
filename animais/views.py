from django.shortcuts import render
from animais.models import Animal

def index(requisicao):
    context = {'caracteristicas': Animal.objects.all()}
    return render(requisicao, 'index.html', context)