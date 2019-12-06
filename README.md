# FOCA DADOS

Repositório para extração, limpeza e análise de dados para o projeto.

## Esse projeto é fruto do Hackfest Rio 2019
O Hackfest 2019 - Um Rio de Dados tem como objetivo fomentar o espírito cívico, o enfrentamento à corrupção e a utilização de tecnologia na promoção de uma sociedade mais participativa.

## API 

Esta API está divida da seguinte forma:

- controller: Pacote responsável por acessar o model e responder as chamadas das rotas;
- model: Pacote responsável por armazenar os modelos para persistência (data)  bem como fazer toda a manipulação necessária no banco de dados.
- route: Pacote responsável por armazenar as rotas das APIs;
- service: Pacote responsável por agregar os serviços da API como crawlers e análise de dados;
- templates: Páginas HTML que interagem com os dados.

## Services

### Analise de dados

Fonte de dados:
- [Eleições 2016 - Votação nominal por município e zona (formato ZIP)](http://agencia.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2016.zip)
- [Eleições 2018 - Votação nominal por município e zona (formato ZIP)](http://agencia.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2018.zip)
- [Mapeamento entre bairros e zonas eleitorais]()

Os dados de votação nominal por município e zona trazem arquivos de todos os estados. Para a aplicação 
nós analisamos apenas o arquivo referente ao estado do Rio de Janeiro fazendo e depois fizemos o filtro para 
o municício de Rio de Janeiro.

Os arquivos separados referente ao estado do Rio de Janeiro também podem ser encontrados [aqui](https://drive.google.com/open?id=1chscZ-xCL2KS--PORm8o2fmiQNecgAP8).
