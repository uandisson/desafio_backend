## Desafio Backend Python


[![Actions Status](https://github.com/uandisson/desafio_backend/workflows/Lint/badge.svg
)](https://github.com/uandisson/desafio_backend/actions)
[![Actions Status](https://github.com/uandisson/desafio_backend/workflows/Python%20Integration%20Test/badge.svg)](https://github.com/uandisson/desafio_backend/actions)
[![Actions Status](https://github.com/uandisson/desafio_backend/workflows/Node.js%20CI/badge.svg)](https://github.com/uandisson/desafio_backend/actions)

## Sobre a Crédito Express

A Crédito Express é uma fintech voltada para servir instituições financeiras. Nosso objetivo é levar TAXAS ATRATIVAS para as pessoas, a partir do uso de tecnologia de ponta.

VENHA FAZER PARTE DESSA REVOLUÇÃO FINANCEIRA!


## Sobre o desafio

Com o aumento dos casos de COVID-19 muitos cidadãos tiveram aumentos nos gastos e redução nos ganhos, levando a eles endividarem-se em meios que as taxas de juros são extremamente altas. Neste desafio você deve construir uma aplicação para pessoas possam simular empréstimos com as melhores taxas do mercado financeiro.

A aplicação deve ter uma API para o cliente informar o seu CPF e numero de celular para se identificar e depois disso ele poderá efetuar simulações de empréstimo em outra API. Para simular é necessário informar o valor do empréstimo e o número de parcelas, sendo que podem ser 6, 12, 18, 24 ou 36.

Existe uma tabela de taxas, o calculo do empréstimo deve ser feito de acordo com ela. Existem 3 tipos diferentes de taxas: **negativado, score alto e score baixo**. Pessoas com score acima de 500 são consideradas com score alto nessa aplicação, pessoas sem cadastro na base recebem score 0.

Após obter o valor da taxa a ser aplicada para esse cliente, será necessário chamar uma API para fazer o cálculo da simulação. Os dados retornados pelo cálculo devem ser o retorno da sua API.


## Considerações

- O arquivo taxas.json possui uma coleção de taxas por característica. Os dados seguem o formato do exemplo abaixo, mas pode modificar a estrutura no seu projeto se precisar:

```javascript
  {
	"tipo": "NEGATIVADO",
	"taxas": {"6": 0.04, "12": 0.045, "18": 0.05, "24": 0.053, "36": 0.055}
  }
```
- O arquivo clientes.json possui uma coleção de objetos que representam os clientes que já tem pré-cadastro. Abaixo temos um exemplo do formato do objeto que também pode ter a estrutura modificada caso julgue necessário.

```javascript
{
	"nome": "Roberto Filipe Figueiredo",
	"cpf": "41882728564",
	"celular": "6526332774",
	"score": 300,
	"negativado": false
}
```

- Abaixo temos um exemplo de um CURL para API de cálculo.

```shell
curl --request POST \
  --url https://us-central1-creditoexpress-dev.cloudfunctions.net/teste-backend \
  --header 'Content-Type: application/json' \
  --data '{
	"numeroParcelas": 12,
	"valor": 10000,
	"taxaJuros": 0.04
}'
```

### Pré-requisitos
- Desenvolvimento de API REST em Python;
- Utilização do MongoDB;
- Desenvolvimento de um Dockerfile/Docker-Compose.yml para rodar o projeto;
- Documentar como rodamos o projeto no README.MD;

### Diferenciais/Extras
- Implementação de Testes de unidade e/ou integração;
- Clean code;
- Segurança e resiliência;
- Utilização de padrões de projeto;
- Migrations e/ou seeders;
- Script para execução da aplicação;

## Pronto para começar o desafio?

- Faça um "fork" deste repositório na sua conta do Github;
- Após completar o desafio, crie um pull request nesse repositório comparando a sua branch com a master com o seu nome no título;



# Uandisson Miranda

## Requisitos

- Python 3.8
- Flask 
- Docker

## 1 - Clone Repositorio:

    $ git clone https://github.com/uandisson/desafio_backend.git
     
## 2 - Buildar o Projeto se quiser !

    obs: Tenha as devidas pastas no seu linux, e nem tente roda no Windows pois o Windows e para os fracos.

    #mkdir /opt/credito-express-app/dev/api
    #chmod +x /opt/credito-express-app/dev/api
    #chmod 777 /opt/credito-express-app/dev/api

    $ cd backend-python/credito-express-app/
    $ sudo docker-compose build

    Caso der erro:

      $ docker-compose build
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.

    Instalando Composer:

    0 - sudo service docker status
    
    1 - sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    2 - sudo chmod +x /usr/local/bin/docker-compose
    3 - docker-compose --version

    Instalando Docker:

    1 - sudo apt-get update -y
    2 - sudo apt-get install -y linux-image-generic-lts-trusty linux-headers-generic-lts-trusty
    3 - sudo apt-get install -y xserver-xorg-lts-trusty libgl1-mesa-glx-lts-trusty
    4 - sudo reboot
    5 - sudo apt-get purge -y lxc-docker* && sudo apt-get -y purge docker.io*
    6 - sudo apt-get update -y && sudo apt-get install -y apt-transport-https ca-certificates
    7 - sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
    8 - sudo apt-get update -y
    9 - sudo apt-cache policy docker-engine 
    10 - sudo apt-get update -y && sudo apt-get install -y linux-image-extra-$(uname -r)
    11 - sudo apt-get install docker-engine -y
    12 - sudo service docker start   
    13 - sudo docker run hello-world
    14 - docker -v
     
## 3 - Iniciar e Debugar

    $ cd backend-python/credito-express-app/
    $ sudo docker-compose up

## 4 - URL -> : http://127.0.0.1:5000

![](imgs/readme_assets/02.png)

## 5 - **Em caso de erro na criação do banco de dados**: Configuração do banco de dados MongoDB

    $ docker exec -it credito_express_mongo bash
    $ mongo -u admin -p
    $ mongodb> use creditoexpressdb
    $ mongodb> db.createUser({user: 'admin', pwd: 'admin', roles: [{role: 'readWrite', db: 'creditoexpressdb'}]})
    $ mongodb> exit
    $ mongo -u admin -p admin --authenticationDatabase creditoexpressdb
    $ mongodb> exit
    $ exit


## Estrutura

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`login` | POST | READ | Login customer
`login/async` | POST | READ | Login customer - asynchronous request
`loan`| POST | READ | Get Tax Customer
`simulation`| POST | READ | Get Amount, Tax and Fees Customer

## Como usar ?

Check customer:
```
    curl -i -H "Content-Type: application/json" -X POST -d '{"cpf": "93762814031", "phone_number": "71935228778"}' http://127.0.0.1:5000/api/v1/login
    
```
get:
```
    {
        "message": "Ok, find custumer", 
        "status": true, 
        "tokens": {
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxMzkzNjU0NywianRpIjoiYjI1ZDAxMjYtN2IwMC00ZDdkLTk1NGMtNTQxNDNmNzM3ZDFjIiwibmJmIjoxNjEzOTM2NTQ3LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiOTM3NjI4MTQwMzEiLCJleHAiOjE2MTQwMjI5NDd9.KsAMmphy71g1nYQPD_wnQ1SsxJBrRGSQ--0r6a6BHCc", 
            "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxMzkzNjU0NywianRpIjoiYmE2NDg4ZDQtNWJjOC00ZDY0LTg2ZDQtYTljZWQxYzY2MzI3IiwibmJmIjoxNjEzOTM2NTQ3LCJ0eXBlIjoicmVmcmVzaCIsInN1YiI6IjkzNzYyODE0MDMxIiwiZXhwIjoxNjE0MDIyOTQ3fQ.jb1kIgJHMEOvgabvgjRCTbmA5FHz4hRBgBoVcxTZgpQ"
        }
    }	

```

do simulation:
```
    curl -i -H "Content-Type: application/json" -X POST -d '{"loan_value": "1000.0", "tax": "0.45", "installments": "6"}' http://127.0.0.1:5000/api/v1/simulation
```
get:
```
    {
        "message": "Loan value: R$ 1000.00\nFees (Tax: 0.45): R$ 27.31\nAmount after (6 months): R$ 1027.31", 
        "status": true
    }

```

tax
```
curl -i -H "Content-Type: application/json" -X POST -d '{"cpf": "93762814031", "phone_number": "71935228778", "installments": "6"}' http://127.0.0.1:5000/api/v1/loan
```
get
```
    {
    "data": 0.04, 
    "status": true
    }

```

tax with JWT
```
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxMzkzNjU0NywianRpIjoiYjI1ZDAxMjYtN2IwMC00ZDdkLTk1NGMtNTQxNDNmNzM3ZDFjIiwibmJmIjoxNjEzOTM2NTQ3LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiOTM3NjI4MTQwMzEiLCJleHAiOjE2MTQwMjI5NDd9.KsAMmphy71g1nYQPD_wnQ1SsxJBrRGSQ--0r6a6BHCc" -H "Content-Type: application/json" -X GET -d '{"cpf": "93762814031", "phone_number": "71935228778", "loan_value": "1000", "installments": "6"}' http://127.0.0.1:5000/api/v1/loan/jwt
```

    OBS: "Authorization: Bearer **Token**" : get in login

get
```
    {
    "data": {
        "12": 0.035, 
        "18": 0.45, 
        "24": 0.048, 
        "36": 0.05, 
        "6": 0.03
    }, 
    "status": true
    }    
```

in the browswer: http://127.0.0.1:5000/index

![](imgs/readme_assets/01.png)

### Swagger
```
http://127.0.0.1:5000

http://127.0.0.1:5000/swagger.json

```

Swagger in the browser

Emdpoints
![](imgs/readme_assets/02.png)

Models

![](imgs/readme_assets/03.png)

# Frontend-Vue

## Requisitos

- Node 14
- Vue JS
- Docker (opcional) -> recomendado

## Executar sem Docker

Instalar dependências
    
    $ npm install

Executar

    $ npm run dev
    
## Executar com Docker

Iniciar e Debugar

    $ cd frontend-vue/
    $ sudo docker-compose up

## URL -> : http://127.0.0.1:8080

Tela inicial

![](imgs/readme_assets/f01.png)

![](imgs/readme_assets/f01-2.png)

Simulação

![](imgs/readme_assets/f02.png)

![](imgs/readme_assets/f03.png)

# Deploy: Amazon EC2 (temporáriamente)

![](imgs/readme_assets/awscloud.svg)

O Amazon Elastic Compute Cloud (Amazon EC2) é um serviço Web que disponibiliza capacidade computacional segura e redimensionável na nuvem. Ele foi projetado para facilitar a computação em nuvem na escala da web para os desenvolvedores. A interface de serviço Web simples do Amazon EC2 permite que você obtenha e configure a capacidade sem muito esforço. Oferece um controle completo de seus recursos computacionais e permite que você trabalhe no ambiente computacional comprovado da Amazon.

## Backend -> : http://3.128.30.149:5000 ou http://ec2-3-128-30-149.us-east-2.compute.amazonaws.com:5000

## Frontend -> : http://3.128.30.149:8080



