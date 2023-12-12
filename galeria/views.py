from django.shortcuts import render

# Funcao que responde a requisicoes
def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')