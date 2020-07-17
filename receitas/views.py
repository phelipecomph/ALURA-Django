from django.shortcuts import render

#Definindo qual é a resposta para a request index criada no arquivo urls.py
def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Sopa de Legumes',
        3: 'Sorvete',
        4: 'Bolo de Chocolate'
    }

    dados = {
        'nome_das_receitas' : receitas
    }

    return render(request,'index.html', dados) #renderizando a pagina templates/index.html

def receita(request):
    return render(request,'receita.html')