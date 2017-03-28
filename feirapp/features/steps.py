import django
django.setup()
from lettuce import *
from rest_framework.test import APIClient, APIRequestFactory
from nose.tools import assert_equals
from feirapp.views import *
from rest_framework import status


@before.all
def set_browser():
    world.browser = APIClient()
    world.factory = APIRequestFactory()


@step(u'Given que algumas feiras estao no sistema')
def given_some_feiras_are_in_the_system(step):
    for data in step.hashes:
        world.response = world.browser.post('/feira/?format=json', data)
        assert_equals(world.response.status_code, status.HTTP_201_CREATED)


@step(u'eu buscar uma Feira com os seguintes parametros:')
def when_eu_buscar_uma_feira(step):
    world.response = world.browser.get('/feira/', step.hashes.first,format='json')
    assert_equals(world.response.status_code, status.HTTP_200_OK)

@step(r'o status do resultado for igual a \'([^\']*)\'')
def then_o_status_do_resultado_for_igual_a_group1(step,expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))


@step(u'valida o retorno')
def and_os_seguintes_resultados_devem_ser_retornados(step):
    # TODO melhorar validacao de retorno - validar o conteudo do retoro
    assert_equals(1, len(world.response.data))


@step(u'Given uma determinada feira \'([^\']*)\'')
def given_uma_determinada_feira_distrito(step, distrito):
    world.response = world.browser.get('/feira/',format='json')
    assert_equals(world.response.status_code, status.HTTP_200_OK)
    #assert False, 'This step must be implemented'


@step(u'When atualizo os campos:')
def when_atualizo_os_campos(step):

    view = FeiraUpdate.as_view()
    request = world.factory.put('feira/update/%d/' % world.response.data[0]['id'],{'numero':'1'})

    # Renderiza Response
    world.response = view(request, pk=world.response.data[0]['id'])
    world.response.render()
    # TODO - melhoria
    assert_equals(world.response.status_code, status.HTTP_200_OK)


@step(u'When eu deleto uma feira')
def when_eu_deleto_uma_feira(step):
    view = FeiraDestroy.as_view()
    request = world.factory.delete('feira/delete/%d/' % world.response.data[0]['id'])

    #renderiza response
    world.response = view(request, pk=world.response.data[0]['id'])
    world.response.render()  # Cannot access `response.content` without this.HTTP_200_OK
    # TODO - melhoria
    assert_equals(world.response.status_code, status.HTTP_204_NO_CONTENT)
