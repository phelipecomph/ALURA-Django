from django.shortcuts import render

#Definindo qual é a resposta para a request index criada no arquivo urls.py
def index(request):
    return render(request,'index.html') #renderizando a pagina templates/index.html