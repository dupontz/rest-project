Feature: Test rest-django with lettuce

Scenario: Test Feira
#Given some feiras are in the system
When I retrieve the feira with distrito 'Vila Formosa'
#Then I should get a '200' response
#And the following user details are returned:
#| name |
#| David Sale |