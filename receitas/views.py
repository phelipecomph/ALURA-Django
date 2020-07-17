from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Receita

#Definindo qual é a resposta para a request index criada no arquivo urls.py
def index(request):
    receitas = Receita.objects.all()

    dados = {
        'receitas' : receitas
    }

    return render(request, 'index.html', dados) #renderizando a pagina templates/index.html

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)