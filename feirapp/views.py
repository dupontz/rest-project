from feirapp.models import Feira
from feirapp.serializers import FeiraSerializer
from rest_framework import generics


class FeiraCreateList(generics.ListCreateAPIView):
    """
    GET: Opcionalmente restringe o resultado de feiras para `distrito`, `regiao5`,`nome_feira`,`bairro`
    POST: Cria uma instancia do objeto no banco de dados.
    """
    # TODO melhoria filtro antes da query - sobrescrever metodo get_queryset

    queryset = Feira.objects.all()
    serializer = FeiraSerializer
    serializer_class = FeiraSerializer
    filter_fields = ('distrito', 'regiao5', 'nome_feira', 'bairro',)


class FeiraDestroy(generics.DestroyAPIView):
    """
     /feira/delete/(?P<pk>\d+)/
    PUT: deleta o registro
    """
    queryset = Feira.objects.all()
    serializer = FeiraSerializer
    serializer_class = FeiraSerializer


class FeiraUpdate(generics.UpdateAPIView):
    """
    /feira/update/(?P<pk>\d+)/
    PUT: atuliza o registro (campos nao obrigatorios)
    """
    queryset = Feira.objects.all()
    serializer = FeiraSerializer
    serializer_class = FeiraSerializer