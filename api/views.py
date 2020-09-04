from django.http import JsonResponse
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from .models import Autor, Noticia
from .serializers import NoticiaSerializer


class NoticiaViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):

    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
def visualizaNoticia(request, pk):
    
    if request.method == 'GET':
        noticia = Noticia.objects.get(pk=pk)
        serializer = NoticiaSerializer(noticia)
        return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def pesquisaNoticia(request):
    if request.method == 'POST':
        if request.data.get('titulo'):
            try:
                titulo = request.data.get('titulo')
                query = Noticia.objects.filter(titulo=titulo).first()
                return JsonResponse(NoticiaSerializer(query).data, safe=False)
            except Noticia.DoesNotExist:
                return JsonResponse(
                    {'error':'Não existe notícia com esse título no Banco de dados'}
                )
        elif request.data.get('texto'):
            try:
                texto = request.data.get('texto')
                query = Noticia.objects.filter(texto=texto).first()
                return JsonResponse(NoticiaSerializer(query).data, safe=False)
            except Noticia.DoesNotExist:
                return JsonResponse(
                    {'error':'Não existe notícia com esse texto no Banco de dados'}
                )
        elif request.data.get('autor'):
            try:
                autor = request.data.get('autor')
                query = Autor.objects.filter(nome=autor).first()
                noticia = Noticia.objects.filter(autor=query)
                return JsonResponse(NoticiaSerializer(noticia, many=True).data, safe=False)
            except Autor.DoesNotExist:
                return JsonResponse(
                    {'error':'Não existe Autor com esse nome no Banco de dados'}
                )
        return JsonResponse(
            {'error': 'Parâmetros não conferem'}
            )