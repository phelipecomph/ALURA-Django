from django.shortcuts import render
from django.http import HttpResponse

#Definindo qual é a resposta para a request index criada no arquivo urls.py
def index(request):
    return HttpResponse('<h1>Receitas</h1> <h2>Bem vindo</h2>') #retornando esse codigo html como resposta