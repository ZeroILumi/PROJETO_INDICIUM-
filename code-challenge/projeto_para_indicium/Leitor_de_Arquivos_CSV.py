# Esta função le o arquivo CSV order_details,
# depois a variavel texto_do_arquivo atribui a si
# o conteudo do arquivo CSV e o divide por espaço depois
# por virgula, a variavel texto atribui a si o Conteúdo Referente
# Aos Campos que serão utilizados no comando CREATE_TABLE
# com seus tipos e as primary key e foreign key,
# O nome dos campos advém dos indices da lista
# texto_do_arquivo
# sendo cada campo um indice de 0 a 4 exceto o campo creation_date
# cuja sua utilidade e registrar a data em que o registro fora efetuado
# para remover as imperfeições do conteudo retornado a variavel
# palavra_1 atribui a si o valor de texto, e palavra_2 atribui a si
# o valor dos erros que no caso [ e ' e para cada indice de palavra_2
# se este indice existe dentro de palavra_1, palavra_1 substitui este
# valor por nada representado por '' depois e retornado o valor de palavra_1
def ler_campos_do_arquivo_csv_para_CREATE_TABLE():
    caminho = '../data/order_details.csv'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    texto_do_arquivo = texto_do_arquivo.split("\n")
    texto_do_arquivo = str(texto_do_arquivo).split(",")
    texto = "   {Chave_Primaria_ID_de_Order_Pedidos} SMALLINT FOREIGN KEY REFERENCES orders(order_id),\n" \
            "   {Chave_Estrangeira_do_ID_de_Products_Produtos} SMALLINT FOREIGN KEY REFERENCES products(product_id),\n" \
            "   {Unit_Price_Preco_Por_Unidade} FLOAT NOT NULL,\n" \
            "   {Quantity_Quantidade_de_Produtos} INT NOT NULL,\n" \
            "   {Discount_Desconto} FLOAT NOT NULL,\n" \
            "   creation_date DATETIME NOT NULL" \
            "".format(Chave_Primaria_ID_de_Order_Pedidos=
                      str(texto_do_arquivo[0]),
                      Chave_Estrangeira_do_ID_de_Products_Produtos=
                      str(texto_do_arquivo[1]),
                      Unit_Price_Preco_Por_Unidade=
                      str(texto_do_arquivo[2]),
                      Quantity_Quantidade_de_Produtos=
                      str(texto_do_arquivo[3]),
                      Discount_Desconto=
                      str(texto_do_arquivo[4]))

    palavra_1 = texto
    palavra_2 = "['"
    for letra in palavra_2:
        if letra in palavra_1:
            palavra_1 = palavra_1.replace(letra, '')
    arquivo.close()
    return palavra_1


# Esta função le os dados no arquivo CSV order_details e
# Coloca estes dados dentro da variavel texto_do_arquivo,
# texto_do_arquivo por sua vez atribui a si seu valor atual
# dividido por espaço e depois faz isso novamente mas desta vez
# dividido por virgula depois a variavel texto atribui a si o valor
# de todos os Campos da tabela separados por virgula e espaço,
# estes valores dos campos vem dos indices da lista texto_do_arquivo
# sendo cada campo um indice de 0 a 4 exceto o campo creation_date
# cuja sua utilidade e registrar a data em que o registro fora efetuado
# para remover as imperfeições do conteudo retornado a variavel
# palavra_1 atribui a si o valor de texto, e palavra_2 atribui a si
# o valor dos erros que no caso [ e ' e para cada indice de palavra_2
# se este indice existe dentro de palavra_1, palavra_1 substitui este
# valor por nada representado por '' depois e retornado o valor de palavra_1
def ler_campos_do_arquivo_csv_para_INSERT_INTO():
    caminho = '../data/order_details.csv'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    texto_do_arquivo = texto_do_arquivo.split("\n")
    texto_do_arquivo = str(texto_do_arquivo).split(",")
    texto = "   {Chave_Primaria_ID_de_Order_Pedidos},\n" \
            "   {Chave_Estrangeira_do_ID_de_Products_Produtos},\n" \
            "   {Unit_Price_Preco_Por_Unidade},\n" \
            "   {Quantity_Quantidade_de_Produtos},\n" \
            "   {Discount_Desconto},\n" \
            "   creation_date\n".format(Chave_Primaria_ID_de_Order_Pedidos=
                                        texto_do_arquivo[0],
                                        Chave_Estrangeira_do_ID_de_Products_Produtos=
                                        texto_do_arquivo[1],
                                        Unit_Price_Preco_Por_Unidade=
                                        texto_do_arquivo[2],
                                        Quantity_Quantidade_de_Produtos=
                                        texto_do_arquivo[3],
                                        Discount_Desconto=
                                        texto_do_arquivo[4])

    palavra_1 = texto
    palavra_2 = "['"
    for letra in palavra_2:
        if letra in palavra_1:
            palavra_1 = palavra_1.replace(letra, '')
    arquivo.close()
    return palavra_1


# Esta função le os dados no arquivo CSV order_details e
# Separa seus dados por espaços depois para cada item antes
# de um espaço ou seja um indice ele começa no alcance(range)
# de 1 pois la começão os Valores(VALUES) a ser inseridos
# em order detais e esse len(texto_do_arquivo)-1
# quer dizer que ele vai repitir ate o limite da minha lista
# e o -1 pois ele começa 1 na frente,-1 é para anular esse fato e não
# faltar Valores, depois eu coloquei para cada repetição o comando de
# INSERT INTO em order_details mais (Com os Campos interpolados dentro)
# os Campos vem do retorno da função ler_campos_do_arquivo_csv_para_INSERT_INTO(),
# depois são inseridos o Valores (Com os Registros interpolados dentro) os
# registros por sua vez vem da repetição do for alterando o indice depois
# if o indice que e x igual a 1 que so sera uma vez e declarada a variavel
# lista_de_comandos como '' que e nada se sem o if ele se apagaria em todas
# as repetições depois lista_de_comandos acrecenta ao seu valor todos os INSERT INTO
# de cada uma das repetições que comandos_insert_into passou no for e
# retorna a lista_de_comandos;
def ler_registros_da_tabela_order_details():
    caminho = '../data/order_details.csv'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    texto_do_arquivo = texto_do_arquivo.split('\n')
    for x in range(1, len(texto_do_arquivo) - 1):
        comandos_insert_into = 'INSERT INTO order_details\n' \
                               '(\n' \
                               '{Campos}' \
                               ')\n' \
                               'VALUES\n' \
                               '(\n' \
                               '    {Registros},GETDATE()\n' \
                               ')\n'.format(Campos=
                                            ler_campos_do_arquivo_csv_para_INSERT_INTO(),
                                            Registros=
                                            texto_do_arquivo[x])
        if x == 1:
            lista_de_comandos = ''
        lista_de_comandos += comandos_insert_into
    arquivo.close()
    return lista_de_comandos


# Esta função le os dados no arquivo categories principal e
# Retorna seus dados;
def ler_arquivo_categories():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/Tabela_categories/categories_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_no_arquivo = arquivo.read()
    arquivo.close()
    return texto_no_arquivo


# Esta função le os dados em um arquivo categories principal antigo e
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_categories_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_categories/' \
              '{data}/categories.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo customer_customer_demo principal e
# Retorna seus dados;
def ler_arquivo_customer_customer_demo():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_customer_customer_demo/' \
              'customer_customer_demo_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo customer_customer_demo principal antigo e
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_customer_customer_demo_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_customer_customer_demo/' \
              '{data}/customer_customer_demo.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo customer_demographics principal e
# Retorna seus dados;
def ler_arquivo_customer_demographics():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_customer_demographics/' \
              'customer_demographics_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo customer_demographics principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_customer_demographics_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_customer_demographics/' \
              '{data}/customer_demographics.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo customers principal e
# Retorna seus dados;
def ler_arquivo_customers():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_customers/' \
              'customers_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo customers principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_customers_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_customers/' \
              '{data}/customers.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo employee_territories principal e
# Retorna seus dados;
def ler_arquivo_employee_territories():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_employee_territories/' \
              'employee_territories_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo employee_territories principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_employee_territories_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_employee_territories/' \
              '{data}/employee_territories.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo employees principal e
# Retorna seus dados;
def ler_arquivo_employees():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_employees/' \
              'employees_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo employees principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_employees_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_employees/' \
              '{data}/employees.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo orders principal e
# Retorna seus dados;
def ler_arquivo_orders():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_orders/' \
              'orders_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo orders principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_orders_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_orders/' \
              '{data}/orders.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo products principal e
# Retorna seus dados;
def ler_arquivo_products():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_products/' \
              'products_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo products principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_products_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_products/' \
              '{data}/products.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo region principal e
# Retorna seus dados;
def ler_arquivo_region():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_region/' \
              'region_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo region principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_region_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_region/' \
              '{data}/region.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo shippers principal e
# Retorna seus dados;
def ler_arquivo_shippers():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_shippers/' \
              'shippers_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo shippers principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_shippers_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_shippers/' \
              '{data}/shippers.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo suppliers principal e
# Retorna seus dados;
def ler_arquivo_suppliers():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_suppliers/' \
              'suppliers_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo suppliers principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_suppliers_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_suppliers/' \
              '{data}/suppliers.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo territories principal e
# Retorna seus dados;
def ler_arquivo_territories():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_territories/' \
              'territories_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo territories principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_territories_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_territories/' \
              '{data}/territories.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados no arquivo us_states principal e
# Retorna seus dados;
def ler_arquivo_us_states():
    caminho = '../data/MICROSOFT_SQL_SERVER/Tabelas/' \
              'Tabela_us_states/' \
              'us_states_COMPLETO.sql'
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo


# Esta função le os dados em um arquivo us_states principal antigo
# Retorna seus dados,
# Referentes a data do passado que foi passada na chamada desta função;
def ler_arquivo_us_states_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_us_states/' \
              '{data}/us_states.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo

def ler_arquivo_order_details_antigo(data):
    data_do_passado = data
    caminho = '../data/MICROSOFT_SQL_SERVER/' \
              'Tabelas/Tabela_order_details/' \
              '{data}/order_details.sql'.format(data=data_do_passado)
    arquivo = open(caminho, 'r')
    texto_do_arquivo = arquivo.read()
    arquivo.close()
    return texto_do_arquivo

if __name__ == "__main__":
    # ler_arquivo_inteiro()
    # ler_arquivo_order_id()
    # ler_arquivo_product_id()
    # ler_arquivo_unit_price()
    # ler_arquivo_quantity()
    # print(ler_arquivo_discount())
    # print(ler_campos_do_arquivo_csv_para_CREATE_TABLE())
    # print(ler_campos_do_arquivo_csv_para_INSERT_INTO())
    # print(ler_registros_da_tabela_order_details())
    print(ler_registros_da_tabela_order_details())
