# Desafio Backend tembici

Desafio tembici, segue abaixo o desafio:
Pense nisso como um projeto de código aberto. Deixa de uma forma que você ficasse impressionado se visse isto no Github. Como isso ficaria, para que você ficasse impressionado se o encontrasse no Github? Agora vá fazer isso.

Tente limitar a quantidade de tempo gasto nisso para no máximo 4 horas. No entanto, sinta-se à vontade para gastar mais - apenas verifique se você está satisfeito com seu envio!

Dica: Estamos procurando um envio de alta qualidade, não uma abordagem do tipo "apenas faça-o". Lembre-se de que este teste é a sua oportunidade de nos mostrar como você pensa; portanto, seja claro sobre como você está pensando em seu código - seja com comentários, testes, como você nomeia coisas etc. Você será avaliado tanto pelas funcionalidade do seu código quanto pela utilização de boas práticas, desenvolva como se fosse um código de produção em um time e não uma prova ou script.

## Environment

Python 3.75  
Django 3.0.5  
[Postman](https://www.postman.com/)

## Installation

Atualizar a SECRET_KEY do arquivo .env (Para teste pode manter o que esta lá)  
Caso contrario pode atualizar utilizando o proprio Django:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copiar a saida do comando e atualiar o arquivo.

### Utilizando o Docker

Instalar Docker:  
[Docker](https://docs.docker.com/get-docker/)

Instalar Docker Compose:  
[DockerCompose](https://docs.docker.com/compose/install/)

```bash
docker-compose up -d
./launch.sh
```

### Executando Localmente

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata viagens/fixtures/inital.json
python manage.py runserver 0.0.0.0:8000
```

## Usage

Importar o Arquivo tembici.postman_collection.json

### Script Postman

* Get Token: Enviando um Json com Username e password retorna o access Token.
* Get Travels: Passando no Token no Cabeçalho, Retorna todas as viagens do Usuario.
* Update Rank: Enviando um Json com o campos a ser atualizado, irá atualizar a viagem que esta parametrizado na URL.
* Get a Travel: Passando o Id da viagem na URL, ele retorna os detalhes.

### Detalhes

Todas as chamadas devem ser parametrizado no Headers o Token do usuario obtido em Get Token.