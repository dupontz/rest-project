Feature: Test rest-django Feira with lettuce

  Scenario: Insere e busca feiras
  Given que algumas feiras estao no sistema
  |long|lat|setcens|areap|coddist |distrito |codsubpref| subprefe | regiao5 | regiao8  | nome_feira |registro | logradouro| bairro | referencia|numero|
  |-46550164|-23558733|355030885000091|3550308005040|87	|VILA FORMOSA|26	|ARICANDUVA-FORMOSA-CARRAO	|Leste|Leste 1|VILA FORMOSA	|4041-0	|RUA MARAGOJIPE	|VL FORMOSA	| TV RUA PRETORIA	|S/N|

  When eu buscar uma Feira com os seguintes parametros:
  |distrito|regiao5|nome_feira| bairro|
  |VILA FORMOSA|Leste |VILA FORMOSA |VL FORMOSA|
  Then o status do resultado for igual a '200'
  And valida o retorno

  Scenario: Atualiza uma feira
  Given uma determinada feira '1'
  When atualizo os campos:
    |distrito|regiao5|nome_feira|bairro|
    |update_distrito|update_regiao5|update_feira5|update_bairro
  Then o status do resultado for igual a '200'

  Scenario: Deleto uma feira
  Given uma determinada feira '1'
  When eu deleto uma feira
  Then o status do resultado for igual a '204'
