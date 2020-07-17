from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #Apontando o index do app, no arquivo views.py
    path('<int:receita_id>', views.receita, name='receita')
]