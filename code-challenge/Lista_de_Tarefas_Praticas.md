2 fontes de dados: banco de dados Postgres, um arquivo CSV.
1.order_detail não existe neste banco de dados.
2.A tabela order_details é representada pelo arquivo CSV.

1.   [X]Extrair dados do banco de dados é gravar no disco local.
	1.[X]Gravar um arquivo para cada tabela eu posso escolher o nome e o formato do arquivo que deseja salvar.
2.   [X]Extrair dados do arquivo CSV é gravar no disco local.
	1.[X]Um arquivo para o arquivo CSV de entrada você pode escolher o nome e o formato do arquivo que deseja salvar.
3.   [X]Extrair dados do banco de dados é gravar num banco de dados de minha escolha.
4.   [X]Extrair dados do arquivo CSV é gravar num banco de dados de minha escolha.
5.   [X]Separar os caminhos de arquivo que eu criei tanto os arquivos de cada tabela tando o arquivo do CSV
	1.[X]A Separação deve ser por tabela e combinação de dias de execução, exemplo:
		/data/postgres/{table}/2021-01-01/file.format
		/data/postgres/{table}/2021-01-02/file.format
		/data/csv/2021-01-02/file.format
6.   [X]Carregar os dados do sistema de arquivos local para o banco de dados final que eu escolhi.
7.   [X]Poder executar uma consulta que mostre os pedidos e seus detalhes.
8.   [X]Os pedidos são colocados em uma tabela chamada "pedidos"no banco de dados Postgres Northwind que veio junto. 
9.   [X]Os detalhes estão colocados no arquivo CSV fornecido, cada linha possui um campo "order_id" apontando para a tabela "pedidos".
10. [X]Construir uma consulta na tabela pedidos no banco de dados que eu escolhi, depende do banco escolhido e de como coloquei os dados la.
11. [X]Extrair todas as tabelas do banco de dados de origem, não importa se você não usará a maioria delas na etapa final. 
12. [X]Fornecer instruções claras sobre como executar todo o pipeline. Quanto mais fácil, melhor.
13. [X]Fornecer um arquivo csv ou json com o resultado da consulta final no banco de dados final.
14. [X]Ser capaz de passar um argumento para o pipeline com um dia do passado e ele deve reprocessar os dados desse dia. Como os dados para este desafio são estáticos, a única diferença para cada dia de execução serão os caminhos de saída.
15. [X] O banco de dados de origem pode ser configurado usando docker compose.
16. [X] Com o docker compose instalado, basta executar:
	docker-compose up
	Eu posso encontrar as credenciais no arquivo docker-compose.yml

