from feirapp.models import Feira
from feirapp.serializers import FeiraSerializer
from rest_framework import generics



class FeiraList(generics.ListAPIView):
    """
            Opcionalmente restringe o resultado de feiras para `distrito`, `regiao5`,`nome_feira`,`bairro`
            Optionally restricts the returned purchases to a given user,
            by filtering against a `username` query parameter in the URL.
            """
    # TODO efetuar filtro antes da query - sobrescrever metodo get_queryset

    queryset = Feira.objects.all()
    serializer = FeiraSerializer
    serializer_class = FeiraSerializer
    filter_fields = ('distrito','regiao5','nome_feira','bairro',)

