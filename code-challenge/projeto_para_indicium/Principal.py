from Classe_criadora_de_comandos_SQL_para_tabelas_em_arquivos import *

# ARQUIVO PRINCIPAL
# onde são executadas todas as tarefas referentes
# A CRIAÇÃO,ESCRITA,PROCESSAMENTO,REPROCESSAMENTO,PESQUISA E LEITURA DE PASTAS E ARQUIVOS.sql
# atravez de funções de um objeto de uma classe com seus metódos
# que estão conectados a diversas funções de outros módulos
# ATENÇÃO pela criação de pastas pedir caminhos exatos talvez
# seja nessario ajustar os caminhos, fora isso tudo foi testado e
# esta funcionando.
# Solução simples para executar o código python
# Devido a peculiaridade de caminhos exatos para a criação de pastas
# Passo 1: Crie uma pasta intitulada como 'Organização da Area de Trabalho Zero ILumi'
# no 'desktop'.
# Passo 2: Dentro de 'Organização da Area de Trabalho Zero ILumi' crie outra pasta intitulada
# como 'Teste pratico indicium'
# Passo 3: Araste a pasta do projeto intitulada como 'code-challenge' para dentro da pasta
# intitulada como 'Teste pratico indicium' e pronto.
# Explicação: Agora você esta usando o mesmo caminho que eu usei então funcionara sem
# alterar o código.

if __name__ == '__main__':
    criador_de_arquivos = Criador_de_pastas_com_a_data_atual_e_arquivos_sql()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_order_details()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_order_details_CSV()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_categories()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_customer_customer_demo()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_customer_demographics()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_customers()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_employee_territories()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_employees()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_orders()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_products()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_region()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_shippers()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_suppliers()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_territories()
    criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_us_states()
    criador_de_arquivos.reprocessar_dados_do_passado(data='07-09-2021')
    criador_de_arquivos.pesquisar_em_orders_por_id('1500')