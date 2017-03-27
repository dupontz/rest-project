from feirapp.models import Feira
from feirapp.serializers import FeiraSerializer
from rest_framework import generics
# Create your views here.
from django.shortcuts import get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import filters
import django_filters
# class CreateList(generics.CreateAPIView):
#     """
#     Create a Feira in the database
#     """
#
# class MultipleFieldLookupMixin(object):
#     """
#     Apply this mixin to any view or viewset to get multiple field filtering
#     based on a `lookup_fields` attribute, instead of the default single field filtering.
#     """
#     def list(self,request):
#         queryset = self.get_queryset()             # Get the base queryset
#         queryset = self.filter_queryset(queryset)  # Apply any filter backends
#         filter = {}
#         for field in self.lookup_fields:
#             if self.kwargs[field]: # Ignore empty fields.
#                 filter[field] = request.query_params[field]
#         return get_list_or_404(queryset, **filter)  # Lookup the object
#
#
#
#
# class RetrieveFeiraView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
#     queryset = Feira.objects.all()
#     serializer_class = FeiraSerializer
#     lookup_field = ('distrito','regiao5 ','nome_feira','bairro')
#
#
# class FeiraList( mixins.ListModelMixin):
#     """
#     Returns all Feira in the database
#     """
#     queryset = Feira.objects.all()
#     serializer_class = FeiraSerializer
#     lookup_fields = ('distrito','regiao5 ','nome_feira','bairro')
#
#     def list(self, request):
#         lookup_fields = ('account', 'username')
#         queryset = self.get_queryset()
#         filter = {}
#         for field in self.lookup_fields:
#                 filter[field] = request.query_params[field]
#
#         #obj =
#         #return obj
#         serializer = FeiraSerializer(get_list_or_404(queryset, **filter), many=True)
#         return Response(serializer.data)
#


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