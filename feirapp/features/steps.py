import django
django.setup()
from lettuce import *
from rest_framework.test import APIClient
from nose.tools import assert_equals
import simplejson as json

@before.all
def set_browser():
    world.browser = APIClient()

@step(u'eu buscar uma Feira com os seguintes parametros:')
def when_eu_buscar_uma_feira_com_group1_igual_a_group2(step):
    world.response = world.browser.get('/feira/?format=json?', step.hashes.first)
#,'regiao5':regiao5,'nome_feira':nome_feira,'bairro':bairro

@step(r'o status do resultado for igual a \'([^\']*)\'')
def then_o_status_do_resultado_for_igual_a_group1(step,expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))


@step(u'And os seguintes resultados devem ser retornados:')
def and_os_seguintes_resultados_devem_ser_retornados(step):
    print json.loads(world.response.content)
    test= world.response.content
    valid ='[{"id":1,"long":-46550164,"lat":-23558733,"setcens":355030885000091,"areap":3550308005040,"coddist":87,"distrito":"VILA FORMOSA","codsubpref":26,"subprefe":"ARICANDUVA-FORMOSA-CARRAO","regiao5":"Leste","regiao8":"Leste 1","nome_feira":"VILA FORMOSA","registro":"4041-0","logradouro":"RUA MARAGOJIPE","numero":"S/N","bairro":"VL FORMOSA","referencia":"TV RUA PRETORIA"},{"id":362,"long":-46534859,"lat":-23562772,"setcens":355030885000038,"areap":3550308005040,"coddist":87,"distrito":"VILA FORMOSA","codsubpref":26,"subprefe":"ARICANDUVA-FORMOSA-CARRAO","regiao5":"Leste","regiao8":"Leste 1","nome_feira":"VILA FORMOSA","registro":"1030-8","logradouro":"AV TRUMAIN C/ HENRIQUE MORIZE","numero":"S/N","bairro":"VL FORMOSA","referencia":"PRACA LIBERIA"}]'
    table ='[{"referencia": "TV RUA PRETORIA", "registro": "4041-0", "regiao5": "Leste", "numero": "S/N", "distrito": "VILA FORMOSA", "setcens": "355030885000091", "nome_feira": "VILA FORMOSA", "logradouro": "RUA MARAGOJIPE", "long": "-46550164", "regiao8": "Leste 1", "coddist": "87", "bairro": "VL FORMOSA", "lat": "-23558733", "subprefe": "ARICANDUVA-FORMOSA-CARRAO", "areap": "3550308005040", "id": "1", "codsubpref": "26"}, {"referencia": "VL FORMOSA", "registro": "1030-8", "regiao5": "Leste", "numero": "PRACA LIBERIA", "distrito": "VILA FORMOSA", "setcens": "355030885000038", "nome_feira": "VILA FORMOSA", "logradouro": "AV TRUMAIN C/ HENRIQUE MORIZE", "long": "-46534859", "regiao8": "Leste 1", "coddist": "87", "bairro": "S/N", "lat": "-23562772", "subprefe": "ARICANDUVA-FORMOSA-CARRAO", "areap": "3550308005040", "id": "362", "codsubpref": "26"}]'
    edittable ='[{"id":1,"long":-46550164,"lat":-23558733,"setcens":355030885000091,"areap":3550308005040,"coddist":87,"distrito":"VILA FORMOSA","codsubpref":26,"subprefe":"ARICANDUVA-FORMOSA-CARRAO","regiao5":"Leste","regiao8":"Leste 1","nome_feira":"VILA FORMOSA","registro":"4041-0","logradouro":"RUA MARAGOJIPE","numero":"S/N","bairro":"VL FORMOSA","referencia":"TV RUA PRETORIA"},{"id":362,"long":-46534859,"lat":-23562772,"setcens":355030885000038,"areap":3550308005040,"coddist":87,"distrito":"VILA FORMOSA","codsubpref":26,"subprefe":"ARICANDUVA-FORMOSA-CARRAO","regiao5":"Leste","regiao8":"Leste 1","nome_feira":"VILA FORMOSA","registro":"1030-8","logradouro":"AV TRUMAIN C/ HENRIQUE MORIZE","numero":"S/N","bairro":"VL FORMOSA","referencia":"PRACA LIBERIA"}]'
    print valid
    print edittable
    assert_equals(edittable, world.response.content)