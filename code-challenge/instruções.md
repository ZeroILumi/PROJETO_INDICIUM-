# <u>Desafio-de-Codigo:</u>

<u>Desafio de código Indicium para desenvolvedor de software com foco em projetos de dados</u>

# <u>Desafio-de-Codigo Técnico da Indicium:</u>

<u>Desafio de código para desenvolvedor de software com foco em projetos de dados.</u>


## <u>Contexto:</u>

<u>Na Indicium temos muitos projetos onde desenvolvemos todo o pipeline de dados para o nosso cliente, desde a extração de dados de várias fontes de dados até o carregamento desses dados em seu destino final, com este destino final variando de um data warehouse para uma ferramenta de Business Intelligency a uma API para integração com sistemas de terceiros.</u>

<u>Como desenvolvedor de software com foco em projetos de dados, sua missão é planejar, desenvolver, implantar e manter um pipeline de dados.</u>


## O Desafio:

Vamos fornecer 2 fontes de dados, um banco de dados Postgres e um arquivo CSV.

O arquivo CSV representa detalhes de pedidos de um sistema de comércio eletrônico.

O banco de dados fornecido é um banco de dados de amostra fornecido pela microsoft para fins educacionais chamado northwind, a única diferença é que a tabela order_detail não existe neste banco de dados que você está recebendo. Esta tabela order_details é representada pelo arquivo CSV que fornecemos.

Esquema do banco de dados Northwind original:

![image](https://user-images.githubusercontent.com/49417424/105997621-9666b980-608a-11eb-86fd-db6b44ece02a.png)

Sua missão é construir um pipeline que extraia os dados todos os dias de ambas as fontes e os grave primeiro no disco local e, depois, em um banco de dados de sua escolha. Para este desafio, o arquivo CSV e o banco de dados serão estáticos, mas em qualquer projeto do mundo real, ambas as fontes de dados estariam mudando constantemente.


É importante que todas as etapas de gravação sejam isoladas umas das outras, você deve ser capaz de executar qualquer etapa sem executar as outras.

Para a primeira etapa, onde você grava dados no disco local, você deve gravar um arquivo para cada tabela e um arquivo para o arquivo CSV de entrada. Este pipeline será executado todos os dias, então deve haver uma separação nos caminhos de arquivo que você criará para cada fonte (CSV ou Postgres), tabela e combinação de dias de execução, por exemplo:

```
/data/postgres/{table}/2021-01-01/file.format
/data/postgres/{table}/2021-01-02/file.format
/data/csv/2021-01-02/file.format
```

você pode escolher o nome e o formato do arquivo que deseja salvar.

## Etapa 2:

Na etapa 2, você deve carregar os dados do sistema de arquivos local para o banco de dados final que você escolheu.

O objetivo final é poder executar uma consulta que mostre os pedidos e seus detalhes. Os pedidos são colocados em uma tabela chamada ** pedidos ** no banco de dados Postgres Northwind. Os detalhes são colocados no arquivo csv fornecido, e cada linha possui um campo ** order_id ** apontando para a tabela ** pedidos **.

Como você vai construir essa consulta dependerá muito de qual banco de dados você escolher e de como você carregará os dados desse banco de dados.

O pipeline será semelhante a este:

![image](https://user-images.githubusercontent.com/49417424/105993225-e2aefb00-6084-11eb-96af-3ec3716b151a.png)



## Requisitos:

- Todas as tarefas devem ser idempotentes, você deve conseguir todo o pipeline por um dia e o resultado deve ser sempre o mesmo
- A etapa 2 depende de ambas as tarefas da etapa 1, portanto, você não deve ser capaz de executar a etapa 2 por um dia se as tarefas da etapa 1 não foram bem-sucedidas
- Você deve extrair todas as tabelas do banco de dados de origem, não importa se você não usará a maioria delas na etapa final.
- Você deve ser capaz de dizer claramente onde o pipeline falhou, para saber a partir de qual etapa você deve executá-lo novamente
- Você deve fornecer instruções claras sobre como executar todo o pipeline. Quanto mais fácil, melhor.
- Você deve fornecer um arquivo csv ou json com o resultado da consulta final no banco de dados final.
- Você não precisa realmente agendar o pipeline, mas deve presumir que ele será executado em dias diferentes.
- Seu pipeline deve estar preparado para funcionar nos últimos dias, o que significa que você deve ser capaz de passar um argumento para o pipeline com um dia do passado e ele deve reprocessar os dados desse dia. Como os dados para este desafio são estáticos, a única diferença para cada dia de execução serão os caminhos de saída.

## Coisas que importam:

- Código limpo e organizado.
- Boas decisões em qual etapa (qual banco de dados, qual formato de arquivo ...) e bons argumentos para apoiar essas decisões.

## Configuração do banco de dados de origem:

O banco de dados de origem pode ser configurado usando docker compose.
Você pode instalar seguindo as instruções em
https://docs.docker.com/compose/install/

Com o docker compose instalado, basta executar

```
docker-compose up
```

Você pode encontrar as credenciais no arquivo docker-compose.yml

## Instrução Final:

Você pode usar qualquer linguagem que desejar, mas lembre-se de que teremos que executar seu pipeline, portanto, escolher uma linguagem ou ferramenta que requeira um ambiente complexo pode não ser uma boa ideia.
Você é livre para usar bibliotecas e estruturas de código aberto, mas também tenha em mente que **você deve escrever código**. Ferramentas de apontar e clicar não são permitidas.

Obrigado por participar!

