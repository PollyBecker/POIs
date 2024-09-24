# POI Management System
Este projeto é um sistema de gerenciamento de Pontos de Interesse (POIs) desenvolvido com **Django** para o backend e **React** para o frontend.
O sistema permite cadastrar, listar e buscar POIs por proximidade.

## Tecnologias Utilizadas
**Backend:** *Django*
**Frontend:** *React*
**Containerização:** *Docker*
**Testes:** *TestCase*
## Funcionalidades
### Backend
**Cadastro de POIs:** Serviço para cadastrar pontos de interesse com os atributos *Nome*, coordenada *X* e coordenada *Y*.
**Listagem de POIs:** Serviço para listar todos os POIs cadastrados.
**Busca por Proximidade:** Serviço para listar POIs próximos a uma coordenada de referência dentro de uma distância máxima.
### Frontend
**Home:** Interface para escolher a opção desejada.
**Cadastro de POIs:** Interface para cadastrar novos POIs.
**Listagem de POIs:** Interface para listar todos os POIs cadastrados.
**Busca por Proximidade:** Interface para buscar POIs próximos a uma coordenada de referência.

***Exemplo de Base de Dados***
*‘Lothlórien’ (x=27, y=12)*
*‘Minas Tirith’ (x=31, y=18)*
*‘Helm’s Deep’ (x=23, y=6)*
*‘Isengard’ (x=28, y=2)*
***Exemplo de Uso***
*Dado o ponto de referência (x=20, y=10) e uma distância máxima de 10 metros, o serviço deve retornar os seguintes POIs:*
*Lothlórien*
*Rivendell*
*Helm’s Deep*

## Como Executar o Projeto
### Pré-requisitos
*Docker* e *Docker Compose* instalados
### Passos
- *Clone o repositório:* git clone https://github.com/PollyBecker/POIs/.git
- *cd seu-repositorio*
- *Verifique se o docker esta ok:* execute um comando de health check de sua preferência como docker run hello-world
- *Configure e inicie os contêineres:* docker-compose up --build

Acesse:
- frontend em http://localhost:3000
- backend em http://localhost:8000/pois/
- swagger em http://localhost:8000/swagger/
- documentação em http://localhost:8000/redoc/

  
