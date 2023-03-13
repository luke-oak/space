from django.shortcuts import render

## DON PRETON
#criando metodo para responder a requisição e abrir o link solicitado



def index(request):
    # DADOS DAS IMAGENS
    dados = {
        1:{"nome": "Nebulosa de Carina",
         "legenda": "webtelescope.org / NASA/ James Webb"},
        2:{"nome": "Galaxia NGC 1079", 
        "legenda" : "nasa.org / NASA / Hubble"}
    }
    return render(request, 'galeria/index.html', {"cards" : dados} )


def imagem(request):
    return render(request, 'galeria/imagem.html')

