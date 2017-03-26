from lettuce import *
from rest_framework.test import APIClient


@before.all
def set_browser():
    world.browser = APIClient()


@step(r'When I retrieve the feira with distrito \'([^\']*)\'')
def when_i_retrieve_the_feira_with_distrito_group1(step, group1):
    world.response = world.app.get('feira/?distrito={}'.format(group1))