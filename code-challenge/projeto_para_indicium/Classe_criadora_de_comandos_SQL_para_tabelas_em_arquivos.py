from Leitor_de_Arquivos_CSV import *
from datetime import *
from Criador_de_Arquivos_sql import *
import os


# Essa classe serve para instanciar objetos referentes a criação
# de pastas com a data atual e arquivos referentes a esta
# mesma data
class Criador_de_pastas_com_a_data_atual_e_arquivos_sql:
    # Método construtor da classe com o proprio objeto futuramente
    # Instanciado como parametro;
    def __init__(self):
        pass

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de order_details dentro do arquivo
    # order_details.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os campos escritos no arquivo order_details.sql
    # são retornados pela função ler_campos_do_arquivo_csv_para_CREATE_TABLE()
    # e todos os comandos de INSERT INTO sãp retornados pela função
    # ler_registros_da_tabela_order_details()
    # posteriormente e criado um arquivo para somente o CREATE TABLE,
    # outro para o INSERT INTO e outro para o CREATE DATABASE utilizando a mesma
    # logica
    def criar_pasta_e_arquivos_com_a_data_atual_para_order_details(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_order_details/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_order_details/{diretorio}/' \
                             'order_details.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write('/*CREATE DATABASE Projeto_Indicium*/\n'
                      'USE Projeto_Indicium\n'
                      'CREATE TABLE order_details\n'
                      '(\n'
                      '{Campos}\n'
                      ')\n'
                      '{INSERT_INTO}'
                      'SELECT * '
                      'FROM order_details'.format(Campos=ler_campos_do_arquivo_csv_para_CREATE_TABLE(),
                                                  INSERT_INTO=ler_registros_da_tabela_order_details()))
        caminho_do_arquivo_de_CREATE_TABLE = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                                             'Tabela_order_details/{diretorio}/' \
                                             'order_details_somente_CREATE_TABLE.sql'.format(
            diretorio=diretorio)
        arquivo_de_CREATE_TABLE = open(caminho_do_arquivo_de_CREATE_TABLE, 'w')
        arquivo_de_CREATE_TABLE.write('/*CREATE DATABASE Projeto_Indicium*/\n'
                                      'USE Projeto_Indicium\n'
                                      'CREATE TABLE order_details\n'
                                      '(\n'
                                      '{Campos}\n'
                                      ')\n'
                                      ''.format(Campos=ler_campos_do_arquivo_csv_para_CREATE_TABLE()))
        caminho_do_arquivo_de_INSERT_INTO = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                                            'Tabela_order_details/{diretorio}/' \
                                            'order_details_somente_INSERT_INTO.sql'.format(
            diretorio=diretorio)
        arquivo_de_INSERT_INTO = open(caminho_do_arquivo_de_INSERT_INTO, 'w')
        arquivo_de_INSERT_INTO.write('/*CREATE DATABASE Projeto_Indicium*/\n'
                                     'USE Projeto_Indicium\n'
                                     '{ler_registros_da_tabela_order_details} SELECT * FROM order_details'
                                     ''.format(
            ler_registros_da_tabela_order_details=ler_registros_da_tabela_order_details()))
        caminho_do_arquivo_de_CREATE_DATABASE = '../data/MICROSOFT_SQL_SERVER/' \
                                                'Tabelas/Tabela_order_details/{diretorio}/' \
                                                'order_details_somente_CREATE_DATABASE.sql'.format(
            diretorio=diretorio)
        arquivo_de_CREATE_DATABASE = open(caminho_do_arquivo_de_CREATE_DATABASE, 'w')
        arquivo_de_CREATE_DATABASE.write('CREATE DATABASE Projeto_Indicium\n'
                                         'USE Projeto_Indicium')
        arquivo.close()
        arquivo_de_CREATE_TABLE.close()
        arquivo_de_INSERT_INTO.close()
        arquivo_de_CREATE_DATABASE.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de categories dentro do arquivo
    # categories.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo categories.sql advém retorno
    # da função ler_arquivo_categories()
    def criar_pasta_e_arquivos_com_a_data_atual_para_categories(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_categories/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_categories/{diretorio}/' \
                             'categories.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_categories())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de customer_customer_demo dentro do arquivo
    # customer_customer_demo.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo customer_customer_demo.sql advém retorno
    # da função ler_arquivo_customer_customer_demo()
    def criar_pasta_e_arquivos_com_a_data_atual_para_customer_customer_demo(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_customer_customer_demo/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_customer_customer_demo/{diretorio}/' \
                             'customer_customer_demo.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_customer_customer_demo())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de customer_demographics dentro do arquivo
    # customer_demographics.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo customer_demographics.sql advém retorno
    # da função ler_arquivo_customer_demographics()
    def criar_pasta_e_arquivos_com_a_data_atual_para_customer_demographics(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_customer_demographics/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_customer_demographics/{diretorio}/' \
                             'customer_demographics.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_customer_demographics())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de customers dentro do arquivo
    # customers.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo customers.sql advém retorno
    # da função ler_arquivo_customers()
    def criar_pasta_e_arquivos_com_a_data_atual_para_customers(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_customers/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_customers/{diretorio}/' \
                             'customers.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_customers())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de employee_territories dentro do arquivo
    # employee_territories.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo employee_territories.sql advém retorno
    # da função ler_arquivo_employee_territories()
    def criar_pasta_e_arquivos_com_a_data_atual_para_employee_territories(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_employee_territories/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_employee_territories/{diretorio}/' \
                             'employee_territories.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_employee_territories())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de employees dentro do arquivo
    # employees.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo employees.sql advém retorno
    # da função ler_arquivo_employees()
    def criar_pasta_e_arquivos_com_a_data_atual_para_employees(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_employees/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_employees/{diretorio}/' \
                             'employees.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_employees())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de orders dentro do arquivo
    # orders.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo orders.sql advém retorno
    # da função ler_arquivo_orders()
    def criar_pasta_e_arquivos_com_a_data_atual_para_orders(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_orders/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_orders/{diretorio}/' \
                             'orders.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_orders())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de products dentro do arquivo
    # products.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo products.sql advém retorno
    # da função ler_arquivo_products()
    def criar_pasta_e_arquivos_com_a_data_atual_para_products(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_products/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_products/{diretorio}/' \
                             'products.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_products())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de region dentro do arquivo
    # region.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo region.sql advém retorno
    # da função ler_arquivo_region()
    def criar_pasta_e_arquivos_com_a_data_atual_para_region(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_region/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_region/{diretorio}/' \
                             'region.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_region())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de shippers dentro do arquivo
    # shippers.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo shippers.sql advém retorno
    # da função ler_arquivo_shippers()
    def criar_pasta_e_arquivos_com_a_data_atual_para_shippers(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_shippers/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_shippers/{diretorio}/' \
                             'shippers.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_shippers())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de suppliers dentro do arquivo
    # suppliers.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo suppliers.sql advém retorno
    # da função ler_arquivo_suppliers()
    def criar_pasta_e_arquivos_com_a_data_atual_para_suppliers(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_suppliers/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_suppliers/{diretorio}/' \
                             'suppliers.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_suppliers())
        arquivo.close()

    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de territories dentro do arquivo
    # territories.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo territories.sql advém retorno
    # da função ler_arquivo_territories()
    def criar_pasta_e_arquivos_com_a_data_atual_para_territories(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_territories/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_territories/{diretorio}/' \
                             'territories.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_territories())
        arquivo.close()

    # Esse Método tem uma varievel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de us_states dentro do arquivo
    # us_states.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os comandos inclusos nesse arquivo us_states.sql advém retorno
    # da função ler_arquivo_us_states()
    def criar_pasta_e_arquivos_com_a_data_atual_para_us_states(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/' \
                            'Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/MICROSOFT_SQL_SERVER/' \
                            'Tabelas/Tabela_us_states/{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
                             'Tabela_us_states/{diretorio}/' \
                             'us_states.sql'.format(
            diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write(ler_arquivo_us_states())
        arquivo.close()

    # A DIFERENÇA DESTE MÉTODO PARA
    # criar_pasta_e_arquivos_com_a_data_atual_para_order_details() e onde ele cria a pasta
    # e os arquivos da mesma ou seja o caminho
    # Esse Método tem uma variavel chamada diretorio que atribui
    # a si a data retornada pela função imprimir_dia_atual()
    # depois cria uma pasta com o nome da data atual
    # através do sistema operacional(operational system) no caso este
    # intitulado como 'os' que chama o caminho(path) e caminho chama juntar(join)
    # para juntar o nome_da_pasta como seu destino final que no caso e onde sera criada
    # a seguir temos o modo de operação na var modo
    # o tentar(try) tenta criar a pasta no caminho informado caso haja um erro
    # no sistema operacional(operational system) ele informa que não foi possivel
    # criar pois a pasta possivelmente ja existe
    # caso não ocorra este erro a pasta sera criada e sera informado este acontecimento
    # ao usuario através de uma impressão(print)
    # após isso através do caminho do arquivo a var arquivo
    # escreve todos os comandos de order_details dentro do arquivo
    # order_details.sql que se encontra na pasta criada anteriormente
    # cada pasta tendo a data atual para fins de pesquisa nos registros,
    # os campos escritos no arquivo order_details.sql
    # são retornados pela função ler_campos_do_arquivo_csv_para_CREATE_TABLE()
    # e todos os comandos de INSERT INTO sãp retornados pela função
    # ler_registros_da_tabela_order_details()
    # posteriormente e criado um arquivo para somente o CREATE TABLE,
    # outro para o INSERT INTO e outro para o CREATE DATABASE utilizando a mesma
    # logica
    def criar_pasta_e_arquivos_com_a_data_atual_para_order_details_CSV(self):
        diretorio = imprimir_dia_atual()
        diretorio_caminho = 'C:/Users/Usuario/Desktop/Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/CSV/' \
                            '{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        caminho_do_arquivo = '../data/CSV/' \
                             '{diretorio}' \
                             '/order_details.sql'.format(diretorio=diretorio)
        arquivo = open(caminho_do_arquivo, 'w')
        arquivo.write('/*CREATE DATABASE Projeto_Indicium*/\n'
                      'USE Projeto_Indicium\n'
                      'CREATE TABLE order_details\n'
                      '(\n'
                      '{Campos}\n'
                      ')\n'
                      '{INSERT_INTO}'
                      'SELECT * '
                      'FROM order_details'.format(Campos=ler_campos_do_arquivo_csv_para_CREATE_TABLE(),
                                                  INSERT_INTO=ler_registros_da_tabela_order_details()))
        caminho_do_arquivo_de_CREATE_TABLE = '../data/CSV/' \
                                             '{diretorio}' \
                                             '/' \
                                             'order_details_somente_' \
                                             'CREATE_TABLE.sql'.format(diretorio=diretorio)
        arquivo_de_CREATE_TABLE = open(caminho_do_arquivo_de_CREATE_TABLE, 'w')
        arquivo_de_CREATE_TABLE.write('/*CREATE DATABASE Projeto_Indicium*/\n'
                                      'USE Projeto_Indicium\n'
                                      'CREATE TABLE order_details\n'
                                      '(\n'
                                      '{Campos}\n'
                                      ')\n'
                                      ''.format(Campos=ler_campos_do_arquivo_csv_para_CREATE_TABLE()))
        caminho_do_arquivo_de_INSERT_INTO = '../data/CSV/' \
                                            '/{diretorio}' \
                                            '/order_details_somente_' \
                                            'INSERT_INTO.sql'.format(diretorio=diretorio)
        arquivo_de_INSERT_INTO = open(caminho_do_arquivo_de_INSERT_INTO, 'w')
        arquivo_de_INSERT_INTO.write('/*CREATE DATABASE Projeto_Indicium*/\n'
                                     'USE Projeto_Indicium\n'
                                     '{ler_registros_da_tabela_order_details} SELECT * FROM order_details'
                                     ''.format(
            ler_registros_da_tabela_order_details=ler_registros_da_tabela_order_details()))
        caminho_do_arquivo_de_CREATE_DATABASE = '../data/CSV/' \
                                                '/{diretorio}' \
                                                '/order_details_' \
                                                'somente_' \
                                                'CREATE_DATABASE.sql'.format(diretorio=diretorio)
        arquivo_de_CREATE_DATABASE = open(caminho_do_arquivo_de_CREATE_DATABASE, 'w')
        arquivo_de_CREATE_DATABASE.write('CREATE DATABASE Projeto_Indicium\n'
                                         'USE Projeto_Indicium')
        arquivo.close()
        arquivo_de_CREATE_TABLE.close()
        arquivo_de_INSERT_INTO.close()
        arquivo_de_CREATE_DATABASE.close()

    # Este método cria uma pasta com a data do passado passada como parametro
    # para ele como nome e depois cria um arquivo nesta pasta e escreve dados referentes
    # a cada uma das tabelas do Banco de dados Projeto_Indicium atravez de funçoes que
    # procurarão pastas em seus diretorios que tenham a mesma data informada como parametro
    def reprocessar_dados_do_passado(self, data):
        diretorio = data
        diretorio_caminho = 'C:/Users/Usuario/Desktop/Organização da Area de Trabalho Zero ILumi/' \
                            'Teste pratico indicium/code-challenge/data/Registros Antigos/' \
                            '{diretorio}'.format(diretorio=diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
        data_do_passado = data
        caminho = 'C:/Users/Usuario/Desktop/Organização da Area de Trabalho Zero ILumi' \
                  '/Teste pratico indicium/code-challenge/data' \
                  '/Registros Antigos/{diretorio}/{data}.sql'.format(data=
                                                                     data_do_passado, diretorio=
                                                                     diretorio)
        arquivo = open(caminho, 'w')
        arquivo.write('/*REGISTROS DE {data}*/\n\n'
                      '/*order_details*/\n'
                      '{order_details_antigo}\n\n'
                      '/*categories*/\n'
                      '{categories_antigo}\n\n'
                      '/*customer_customer_demo*/\n'
                      '{customer_customer_demo_antigo}\n'
                      '/*customer_demographics*/\n'
                      '{customer_demographics_antigo}\n\n'
                      '/*customers*/\n'
                      '{customers_antigo}\n\n'
                      '/*employee_territories*/\n'
                      '{employee_territories_antigo}\n\n'
                      '/*employees*/\n'
                      '{employees_antigo}\n\n'
                      '/*orders*/\n'
                      '{orders_antigo}\n\n'
                      '/*products*/\n'
                      '{products_antigo}\n\n'
                      '/*region*/\n'
                      '{region_antigo}\n\n'
                      '/*shippers*/\n'
                      '{shippers_antigo}\n\n'
                      '/*suppliers*/\n'
                      '{suppliers_antigo}\n\n'
                      '/*territories*/\n'
                      '{territories_antigo}\n\n'
                      '/*us_states*/\n'
                      '{us_states_antigo}\n\n'.format(data=data_do_passado,
                                                      categories_antigo=ler_arquivo_categories_antigo(data),
                                                      customer_customer_demo_antigo=ler_arquivo_customer_customer_demo_antigo(
                                                          data),
                                                      customer_demographics_antigo=ler_arquivo_customer_demographics_antigo(
                                                          data),
                                                      customers_antigo=ler_arquivo_customers_antigo(data),
                                                      employees_antigo=ler_arquivo_employees_antigo(data),
                                                      orders_antigo=ler_arquivo_orders_antigo(data),
                                                      products_antigo=ler_arquivo_products_antigo(data),
                                                      region_antigo=ler_arquivo_region_antigo(data),
                                                      shippers_antigo=ler_arquivo_shippers_antigo(data),
                                                      suppliers_antigo=ler_arquivo_suppliers_antigo(data),
                                                      territories_antigo=ler_arquivo_territories_antigo(data),
                                                      us_states_antigo=ler_arquivo_us_states_antigo(data),
                                                      employee_territories_antigo=ler_arquivo_employee_territories_antigo(
                                                          data),
                                                      order_details_antigo=ler_arquivo_order_details_antigo(data)))

        arquivo.close()

    # Essa função pesquisa em orders pelo seu id e escreve um arquivo com
    # o nome como id_ e o valor que foi passado para id depois escreve nesse
    # arquivo um SELECT * FROM orders e pesquisa campos onde o id seja igual
    # ao parametro da função
    def pesquisar_em_orders_por_id(self, id):
        caminho = '../Pesquisas_em_order_por_id/id_{id}.sql'.format(id=id)
        arquivo = open(caminho, 'w')
        arquivo.write('SELECT *\n'
                      'FROM orders\n'
                      'WHERE order_id = {id}'.format(id=id))


if __name__ == "__main__":
    criador_de_arquivos = Criador_de_pastas_com_a_data_atual_e_arquivos_sql()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_order_details()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_order_details_CSV()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_categories()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_customer_customer_demo()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_customer_demographics()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_customers()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_employee_territories()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_employees()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_orders()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_products()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_region()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_shippers()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_suppliers()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_territories()
    # criador_de_arquivos.criar_pasta_e_arquivos_com_a_data_atual_para_us_states()
    # criador_de_arquivos.reprocessar_dados_do_passado(data='07-09-2021')
    criador_de_arquivos.pesquisar_em_orders_por_id('10500')
