from feirapp.models import Feira
from feirapp.serializers import FeiraSerializer
from rest_framework import generics

import logging
log = logging.getLogger(__name__)
class FeiraCreateList(generics.ListCreateAPIView):
    """
    GET: Opcionalmente restringe o resultado de feiras para `distrito`, `regiao5`,`nome_feira`,`bairro`
    POST: Cria uma instancia do objeto no banco de dados.
    """
    # TODO melhoria de filtro da query - sobrescrever metodo get_queryset

    queryset = Feira.objects.all()
    serializer = FeiraSerializer
    serializer_class = FeiraSerializer
    filter_fields = ('distrito', 'regiao5', 'nome_feira', 'bairro',)

    def perform_create(self,serializer):
        instance = serializer.save()
        user = self.request.user
        logging.info('ID={0} salvo com sucesso por {1}'.format(instance.id,user))

class FeiraDestroy(generics.DestroyAPIView):
    """
     /feira/delete/(?P<pk>\d+)/
    PUT: deleta o registro
    """
    queryset = Feira.objects.all()
    serializer = FeiraSerializer
    serializer_class = FeiraSerializer
    def perform_destroy(self, serializer):
        instance = serializer.save()
        user = self.request.user
        logging.info('ID={0} deletado com sucesso por {1}'.format(serializer.id,user) )
   
class FeiraUpdate(generics.UpdateAPIView):
    """
    /feira/update/(?P<pk>\d+)/
    PUT: atuliza o registro (campos nao obrigatorios)
    """
    queryset = Feira.objects.all()
    serializer = FeiraSerializer
    serializer_class = FeiraSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        user = self.request.user
        logging.info('ID={0} atualizado com sucesso por {1}'.format(instance.id,user))

