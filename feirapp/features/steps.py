import django
django.setup()
from lettuce import *
from rest_framework.test import APIClient
from nose.tools import assert_equals
import json as json
from rest_framework import status
from django.core.management import call_command


@before.all
def set_browser():
    world.browser = APIClient()


@step(u'Given que algumas feiras estao no sistema')
def given_some_feiras_are_in_the_system(step):
    for data in step.hashes:
        world.response = world.browser.post('/feira/?format=json', data)
        assert_equals(world.response.status_code, status.HTTP_201_CREATED)


@step(u'eu buscar uma Feira com os seguintes parametros:')
def when_eu_buscar_uma_feira_com_group1_igual_a_group2(step):
    world.response = world.browser.get('/feira/?format=json?', step.hashes.first)

@step(r'o status do resultado for igual a \'([^\']*)\'')
def then_o_status_do_resultado_for_igual_a_group1(step,expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))


@step(u'valida o retorno')
def and_os_seguintes_resultados_devem_ser_retornados(step):
    # TODO melhorar validacao de retorno - validar o conteudo do retoro
    assert_equals(1, len(world.response.data))


@step(u'Given uma determinada feira \'([^\']*)\'')
def given_uma_determinada_feira_distrito(step, group1):
    assert False, 'This step must be implemented'


@step(u'When atualizo os campos:')
def when_atualizo_os_campos(step):
    assert False, 'This step must be implemented'
