# Denox API
A API recebe dados cartográficos do MongoDB, processa-os e então guarda em outra coleção.

## Instruções
Execute `docker-compose build` para buildar a imagem do Docker e então `docker-compose up` para rodar o banco e a API no Docker. 

Também é possível fazer o ambiente local, com `pipenv install`, para instalar e `pipenv run python ./src/main.py` para executar. Alternativamente, pode-se primeiro entrar no ambiente virtual e então executar por ele
```
pipenv shell
python ./src/main.py
```
