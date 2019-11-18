# API FOCA DADOS

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