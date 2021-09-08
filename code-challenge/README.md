# 					                        PROJETO INDICIUM 



### O Programa para Criar,LER,ESCREVER,PROCESSAR,REPROCESSAR, e PESQUISAR pastas e arquivos.sql se encontra no diretório 'projeto_para_indicium' foi escrito em python, os arquivos.sql foram criados para o banco de dados Microsoft SQL Server, e utilizei a IDE PyCharm para escrever meus arquivos python, e o SGBD SQL Server Management Studio para criar as tabelas e realizar pesquisas no banco de dados a fim de testar o mesmo, apesar de utilizar diversos módulos para o desenvolvimento desta solução coloquei as funções de suma importancia em um só arquivo que e o 'Principal.py' porém estas funções dependem de outras para funcionar estas estão nos outros arquivos comentei o código de uma maneira relativamente compreensível,em 'Pesquisas_em_order_por_id' são se encontra as pesquisas escritas pela função pesquisar_em_orders_por_id(id), em

### Registro de comandos SQL utilizados a somente comandos para criação e utilização de um banco de dados dentro do SGBD SQL Server Management Studio,  em 'Exemplo_de_Query_em_orders_pelo_order_id_com_where.sql' temos um exemplo de pesquisa(query) em orders pelo seu id, e resultado dessa pesquisa em CSV no arquivo 'Exemplo_de_Query_em_orders_pelo_order_id_com_where.csv',temos um exemplo de pesquisa em products em 'Exemplo_de_Query_em_products_pelo_product_id_com_where.sql',

### O arquivo data contém o banco de dados 'northwind' em 'northwind.sql' que através de uma conversão manual no mesmo criei sua versão Microsoft SQL Server no arquivo 'northwind_re-escrito_no_Microsoft_SQL_Server_com_order_details_funcional.sql' com um extra a tabela order_details que fora extraída do arquivo CSV 'order_details.csv', em Registros Antigos se encontra os dados reprocessados de todas as tabelas na data que foi informada para a função reprocessar_dados_do_passado(data) exemplo: reprocessar_dados_do_passado(data='10-09-2021') para o reprocessamento ocorrer o dado desta data precisa existir originalmente, no diretório 'CSV' se encontra um outro diretório contendo a data atual e datas do passado com as tabelas de order_details geradas a partir do anteriormente mencionado arquivo 'order_details.csv', essas tabelas tanto possuem um principal com todos os comandos tanto partes da mesma com só o comando de CREATE TABLE ou só o comando de CREATE DATABASE ou só o comando de INSERT INTO VALUES,O diretório MICROSOFT_SQL_SERVER armazena um outro diretório o 'Tabelas' este contém os dados de todas as tabelas do banco de dados completas e em partes e também guarda registos com a data atual e datas passadas das mesmas em seus respectivos diretórios,obrigado por terem lido.

# Solução simples para executar o código python 

# Devido a peculiaridade de caminhos exatos para a criação de pastas 

## Passo 1: Crie uma pasta intitulada como 'Organização da Area de Trabalho Zero ILumi' no 'desktop'.

## Passo 2: Dentro de 'Organização da Area de Trabalho Zero ILumi' crie outra pasta intitulada como 'Teste pratico indicium'

## Passo 3: Araste a pasta do projeto intitulada como 'code-challenge' para dentro da pasta intitulada como 'Teste pratico indicium' e pronto.

## Explicação: Agora você esta usando o mesmo caminho que eu usei então funcionara sem alterar o código

