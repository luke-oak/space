from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

## DON PRETON
#criando metodo para responder a requisição e abrir o link solicitado



def index(request):
    # DADOS DAS IMAGENS
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards" : fotografias} )


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

