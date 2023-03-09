from django.shortcuts import render

## DON PRETON
#criando metodo para responder a requisição e abrir o link solicitado
def index(request):
    return render(request, 'galeria/index.html')


def imagem(request):
    return render(request, 'galeria/imagem.html')