# Executar testes

	python manage.py harvest --test-server --no-server

# Executar projeto 

	python manage.py makemigrations 
	python manage.py make
	python manage.py runserver

# Script para carga de banco
	python import_db.py


# Como usar a API

### Inserir um feira

Request:


	POST /feira/?format=json


Requet data:
```
{
        "long": -46550164,
        "lat": -23558733,
        "setcens": 355030885000091,
        "areap": 3550308005040,
        "coddist": 87,
        "distrito": "VILA FORMOSA",
        "codsubpref": 26,
        "subprefe": "ARICANDUVA-FORMOSA-CARRAO",
        "regiao5": "Leste",
        "regiao8": "Leste 1",
        "nome_feira": "VILA FORMOSA",
        "registro": "4041-0",
        "logradouro": "RUA MARAGOJIPE",
        "numero": "S/N",
        "bairro": "VL FORMOSA",
        "referencia": "TV RUA PRETORIA"
}
```
Response status: 201

Response data:
```
{
	'referencia': u'TV RUA PRETORIA', 
	'registro': u'4041-0', 
	'regiao5': u'Leste', 
	'numero': u'S/N', 
	'distrito': u'VILA FORMOSA', 
	'setcens': 355030885000091, 
	'nome_feira': u'VILA FORMOSA', 
	'logradouro': u'RUA MARAGOJIPE', 
	'long': -46550164, 
	'regiao8': u'Leste 1', 
	'coddist': 87, 
	'bairro': u'VL FORMOSA', 
	'lat': -23558733, 
	'subprefe': u'ARICANDUVA-FORMOSA-CARRAO', 
	'areap': 3550308005040, 
	'id': 881, 
	'codsubpref': 26
}
```
### Lista feiras

Request:

	GET /feira/?format=json
    GET /feira/?distrito=(?P<distrito>\d+)&format=json
    GET /feira/?distrito=(?P<distrito>\d+)&regiao5=(?P<regiao5>\d+)&nome_feira=(?P<nome_feira>\d+)&bairro=(?P<bairro>\d+)&format=json
Response status: 200

Response data:
```
[
    {
        "id": 1,
        "long": -46550164,
        "lat": -23558733,
        "setcens": 355030885000091,
        "areap": 3550308005040,
        "coddist": 87,
        "distrito": "VILA FORMOSA",
        "codsubpref": 26,
        "subprefe": "ARICANDUVA-FORMOSA-CARRAO",
        "regiao5": "Leste",
        "regiao8": "Leste 1",
        "nome_feira": "VILA FORMOSA",
        "registro": "4041-0",
        "logradouro": "RUA MARAGOJIPE",
        "numero": "S/N",
        "bairro": "VL FORMOSA",
        "referencia": "TV RUA PRETORIA"
    },
    .
    .
    .
]
```


### Atualizar um feira

Request:

	PUT /feira/update/(?P<pk>\d+)/?format=json

	PUT /feira/update/1/?format=json

Request data:
```
{  
    "long": -46550164,
    "lat": -23558733,
    "setcens": 355030885000091,
    "areap": 3550308005040,
    "coddist": 87,
    "distrito": "VILA FORMOSA",
    "codsubpref": 26,
    "subprefe": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste",
    "regiao8": "Leste 1",
    "nome_feira": "VILA FORMOSA",
    "registro": "4041-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "S/N",
    "bairro": "VL FORMOSA",
    "referencia": "TV RUA PRETORIA"
}
```
Response Status: 200

Response data:
```
{
	'referencia': u'TV RUA PRETORIA', 
	'registro': u'4041-0', 
	'regiao5': u'Leste', 
	'numero': u'S/N', 
	'distrito': u'VILA FORMOSA', 
	'setcens': 355030885000091, 
	'nome_feira': u'VILA FORMOSA', 
	'logradouro': u'RUA MARAGOJIPE', 
	'long': -46550164, 
	'regiao8': u'Leste 1', 
	'coddist': 87, 
	'bairro': u'VL FORMOSA', 
	'lat': -23558733, 
	'subprefe': u'ARICANDUVA-FORMOSA-CARRAO', 
	'areap': 3550308005040, 
	'id': 881, 
	'codsubpref': 26
}
```
### Deletar uma feira 

Request:

	DELETE /feira/update/(?P<pk>\d+)/?format=json

	DELETE /feira/update/1/?format=json

Response Status: 204

Response data: 

	''


### Para mais informações sobre metodos disponiveis

Request:

	OPTIONS /feira/

	OPTIONS /feira/update/1

	OPTIONS /feira/delete/1
