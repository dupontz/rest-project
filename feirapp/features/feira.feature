Feature: Test rest-django with lettuce

Scenario: Test list de Feiras com filtros
#Given some feiras are in the system
When eu buscar uma Feira com os seguintes parametros:

|distrito|regiao5|nome_feira| bairro|
|VILA FORMOSA|Leste |VILA FORMOSA |VL FORMOSA|
Then o status do resultado for igual a '200'
And os seguintes resultados devem ser retornados:
|id|long|lat|setcens|areap|coddist |distrito |codsubpref| subprefe | regiao5 | regiao8  | nome_feira |registro | logradouro| bairro | referencia|numero|
|1|-46550164|-23558733|355030885000091|3550308005040|87	|VILA FORMOSA|26	|ARICANDUVA-FORMOSA-CARRAO	|Leste|Leste 1|VILA FORMOSA	|4041-0	|RUA MARAGOJIPE	|VL FORMOSA	| TV RUA PRETORIA	|S/N|
|362|-46534859| -23562772|355030885000038|3550308005040|87|VILA FORMOSA|26|ARICANDUVA-FORMOSA-CARRAO|Leste|Leste 1|VILA FORMOSA|1030-8|AV TRUMAIN C/ HENRIQUE MORIZE|VL FORMOSA|PRACA LIBERIA| S/N|
#| David Sale |