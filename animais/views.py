from django.shortcuts import render
from animais.models import Animal

def index(requisicao):
    context = {'caracteristicas': None}
    if 'buscar' in requisicao.GET:
        animais = Animal.objects.all()
        animal_pesquisado = requisicao.GET['buscar']
        caracteristicas = animais.filter(nome_animal__icontains = animal_pesquisado)
        context = {'caracteristicas': caracteristicas}
    return render(requisicao, 'index.html', context)