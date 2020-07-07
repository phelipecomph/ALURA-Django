from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('receitas.urls')), #incluindo todos os urls do app receitas ao path ''
    path('admin/', admin.site.urls),
]
