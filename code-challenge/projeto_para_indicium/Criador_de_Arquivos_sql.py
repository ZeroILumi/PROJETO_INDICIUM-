from Leitor_de_Arquivos_CSV import *
from datetime import *
import os

def criar_banco_de_dados_projeto_para_indicium_e_utilizalo():
     caminho = 'C:/Users/Usuario/Desktop/Organização da Area de Trabalho Zero ILumi' \
               '/Teste pratico indicium/code-challenge/data/Tabelas' \
               '/Comando_para_criar_e_usar_banco_de_dados_Projeto_Indicium.sql'
     arquivo = open(caminho, 'w')
     arquivo.write('CREATE DATABASE Projeto_Indicium\n'
                   'USE Projeto_Indicium')




def criar_comandos_de_criacao_da_tabela_order_details():
    caminho = 'C:/Users/Usuario/Desktop/Nova pasta/Tabela_order_details.sql'
    arquivo = open(caminho, 'w')
    arquivo.write('CREATE TABLE order_details\n'
                  '(\n'
                  '{Campos}\n'
                  ')\n'
                  ''.format(Campos=ler_campos_do_arquivo_csv_para_CREATE_TABLE()))


def criar_registos_da_tabela_order_details():
    caminho = 'C:/Users/Usuario/Desktop/Nova pasta/Registros_da_tabela_order_details.sql'
    arquivo = open(caminho, 'w')
    arquivo.write('{ler_registros_da_tabela_order_details} SELECT * FROM order_details'
                  ''.format(ler_registros_da_tabela_order_details=ler_registros_da_tabela_order_details()))


# Esta função atraves da variavel hoje
# atribui a si a data atual que e retornada
# pela função do datatime datetime.now()
# depois a função retorna a data atual formatada
# em str de tempo com o dia-mes-ano_completo
# exemplo 10-09-2021
def imprimir_dia_atual():
    hoje = datetime.now()
    return hoje.strftime('%d-%m-%Y')


def criar_pasta_e_arquivo_com_a_data_atual_para_order_detais():
    diretorio = imprimir_dia_atual()
    diretorio_caminho = 'C:/Users/Usuario/Desktop/Organização da Area de Trabalho Zero ILumi/' \
                        'Teste pratico indicium/code-challenge/data/' \
                        'Tabela_order_details/{diretorio}'.format(diretorio=diretorio)
    caminho = os.path.join(diretorio, diretorio_caminho)
    modo = 0o166
    try:
        os.mkdir(caminho, modo)
    except OSError:
        print('Não foi possivel criar a Pasta {nome_da_pasta}'
              ' possivelmente ela ja existe.'.format(nome_da_pasta=diretorio))
    else:
        print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=diretorio))
    caminho_do_arquivo = 'C:/Users/Usuario/Desktop/Organização da Area de Trabalho Zero ILumi' \
                         '/Teste pratico indicium/code-challenge/data/' \
                         'Tabela_order_details/{diretorio}' \
                         '/order_detais.txt'.format(diretorio=diretorio)
    arquivo = open(caminho_do_arquivo, 'w')
    arquivo.write("aaaa")


if __name__ == '__main__':
    # criar_comandos_de_criacao_da_tabela_order_details()
    # criar_registos_da_tabela_order_details()
    # criar_pasta_e_arquivo_com_a_data_atual_para_order_detais()
    criar_banco_de_dados_projeto_para_indicium_e_utilizalo()
