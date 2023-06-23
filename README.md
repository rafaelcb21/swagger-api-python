# Invoice Management API

## Cenário
O cliente precisa controlar por meio de relatórios as Notas Fiscais emitidas, para que dessa forma consiga se planejar, mitigando o risco de desenquadramento contábil.
Nesse cenário o cliente emiti diveras NF no qual estão atreladas a inúmeras empresas e categorias, e por causa disso, existe a necessidade de administrar as categorias contábeis, as empresas das receitas (NF) e despesas contábeis.

## Proposta no backend
Ao atuar no cenário descrito, foi desenvolvido uma API que irá receber os dados do frontend, irá armazena-los em um banco de dados, e irá responder as solicitações do frontend, tudo isso utilizando a autenticação JWT.

## Requisições
São no total 26 requisições (GET POST, PUT, DELETE) que o frontend irá demandar a API, divididas em 8 categorias: Authentication, User, Customer, Category, Expense, Revenue, Report, Setting.

## Horas / Atividades
- 05h / Estudo (mini prototipos) e escolha da tecnologia que será usada para solucinar o problema do cliente no prazo
- 07h / Construção da documentação da API
- 15h / Desenvolvimento da funcionalidade para cada requisição que a API irá receber
- 05h / Criar testes automatizados e carregamento de dados automatizados no database, facilitando a realização dos testes
- 03h / Criar a documentação para utilização da API

## Estimativa de dias
- Serão necessários 7 dias corridos, trabalhando 35h nesse período para entregar a API funcionando

## Instalação da API

### Requerimentos
- Python 3.5.2+ : Download - [Python 3](https://www.python.org/downloads/)
- Git - [download](https://git-scm.com/download/win)

### Instalação

1. Clonar o projeto:
```bash
git clone https://git.vibbra.com.br/rafael-1686957388/invoice-management-api.git
cd invoice-management-api
```

2. Crie o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate
``` 
Irá aparecer no inicio da linha de comando a seguinte informação `(venv)`

3.  Instale todas as dependências do projeto no ambiente virtual:
```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` com as seguintes chaves:
```
VERSION=1
SECRET_KEY='<chave_secreta>'
TOKEN_TEST=
```
O token é obtido ao utilizar o endpoint `/api/v1/auth POST`
resposta:
```json
{
  "token": "token",
  "user": {
    "cnpj": "cnpj",
    "company_name": "company_name",
    "email": "email",
    "name": "name",
    "password": "password",
    "phone_number": "phone_number"
  }
}
```
Só é necessário esse token no `.env` quando for executar os testes automatizados

5. Iniciar a API
```bash
python -m swagger_server
```
A interface gráfica é a documentação do swagger que se encontrará no endereço [http://127.0.0.1:8080/ui](http://127.0.0.1:8080/ui)

6. Carga no banco de dados
Para visualizar o funcionamento da API no primeiro momento, é possivel carregar alguns dados automaticamente e dessa forma adquirir o Token:

- Abra outro terminal e vá até o diretorio `invoice-management-api`
- execute os comandos:
```bash
# Para entrar no ambiente virtual
.\venv\Scripts\activate

# Para carregar os dados
python test_initial_database_load.py
```

Dessa forma já será possivel testar a API com o cliente

### Testes Automatizados

Na construção da API foram realizados muitos testes manuais, contudo a automatização dos testes é um tópico que esta em desenvolvimento.
Foi criado para os 2 endpoints do Setting, 6 testes automatizados.
Para executa-los, insira o comando abaixo no terminal:
```bash
# Estando na raiz do projeto
cd swagger_server\test
python -m unittest test_setting.py

# Para executar todos os testes desse diretorio
cd swagger_server
python -m unittest discover .\test\
```

### Futuras melhorias
- Realizar mais testes automatizados
- Todo o projeto é autenticado por JWT usando a SECRET_KEY, contudo para de fato ser mais seguro, é necessário trocar a SECRET_KEY por chaves publicas e chaves privadas. Esse desenvolvimento não foi possivel realizar no prazo estimado.
- Salvar a senha com SALT e Criptografia

## Demonstração
Assista o video do processo de instalação e da utilização da API no seguinte [endereço](https://youtu.be/NXnNol1r6bU)
Caso não consiga assistir, ele está no meu canal do Youtube - [Channel](https://www.youtube.com/channel/UCyDTBjGldpqvXKF3LDZCgnQ)