from django.shortcuts import render
from animais.models import Animal

def index(request):
    animais = Animal.objects.all()
    context = {'caracteristicas' : animais}

    if 'buscar' in request.GET:
        animal_pesquisado = request.GET['buscar']
        caracteristicas = animais.filter(nome_animal__icontains = animal_pesquisado)
        context = {'caracteristicas': caracteristicas}
    return render(request, 'index.html', context)