from django.urls import path

# DON PRETON

#importando os metodos para ir até o link
from galeria.views import index, imagem

#definindo caminhos
urlpatterns = [
    path('', index, name='index'),
    #sempre que houver uma requisição de imagem quem atenderá será o arquivo 'imagem'
    path('imagem/<int:foto_id>', imagem, name ='imagem')
]

# DON PRETON