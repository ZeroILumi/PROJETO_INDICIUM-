# REGISTO DE CODIGO NÃO UTILIZADO
# Registros = {
#     'Chave_Primaria_ID_de_Order_Pedidos':
#         lambda lista: [str(lista[x]) for x in range(5, len(lista), 5)],
#     'Chave_Estrangeira_do_ID_de_Products_Produtos':
#         lambda lista: [str(lista[x]) for x in range(6, len(lista), 5)],
#     'Unit_Price_Preco_Por_Unidade':
#         lambda lista: [str(lista[x]) for x in range(7, len(lista), 5)],
#     'Quantity_Quantidade_de_Produtos':
#         lambda lista: [str(lista[x]) for x in range(8, len(lista), 5)],
#     'Discount_Desconto':
#         lambda lista: [str(lista[x]) for x in range(9, len(lista), 5)]
# }
# registros_de_Chave_Primaria_ID_de_Order_Pedidos = Registros[
#     'Chave_Primaria_ID_de_Order_Pedidos']
# registros_de_Chave_Estrangeira_do_ID_de_Products_Produtos = Registros[
#     'Chave_Estrangeira_do_ID_de_Products_Produtos']
# registros_de_Unit_Price_Preco_Por_Unidade = Registros[
#     'Unit_Price_Preco_Por_Unidade']
# registros_de_Quantity_Quantidade_de_Produtos = Registros[
#     'Quantity_Quantidade_de_Produtos']
# registros_de_Discount_Desconto = Registros[
#     'Discount_Desconto']
# for x in range(5, len(texto_do_arquivo_organizado), 5):
#     registros_de_Chave_Primaria_ID_de_Order_Pedidos = texto_do_arquivo_organizado[
#         x in range(5, len(texto_do_arquivo_organizado))]
#     registros_de_Chave_Estrangeira_do_ID_de_Products_Produtos = texto_do_arquivo_organizado[
#         x in range(6, len(texto_do_arquivo_organizado))]
#     registros_de_Unit_Price_Preco_Por_Unidade = texto_do_arquivo_organizado[
#         x in range(7, len(texto_do_arquivo_organizado))
#     ]
#     registros_de_Quantity_Quantidade_de_Produtos = texto_do_arquivo_organizado[
#         x in range(8, len(texto_do_arquivo_organizado))
#     ]
#     registros_de_Discount_Desconto = texto_do_arquivo_organizado[
#         x in range(9, len(texto_do_arquivo_organizado))
#     ]

# def ler_arquivo_inteiro():
#     caminho = '../data/order_details.csv'
#     arquivo = open(caminho, "r")
#     texto_do_arquivo = arquivo.read()
#     texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#     print(texto_do_arquivo_organizado[0])
#     for x in range(1, len(texto_do_arquivo_organizado)):
#         print(texto_do_arquivo_organizado[x])
#     arquivo.close()
#
#
# def ler_arquivo_order_id():
#     caminho = '../data/order_details.csv'
#     arquivo = open(caminho, "r")
#     texto_do_arquivo = arquivo.read()
#     texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#     texto_do_arquivo_organizado_mais_ainda_str = str(texto_do_arquivo_organizado)
#     texto_do_arquivo_organizado_mais_ainda = texto_do_arquivo_organizado_mais_ainda_str.split(",")
#     for x in range(0, len(texto_do_arquivo_organizado), 5):
#         print(texto_do_arquivo_organizado_mais_ainda[x])
#     arquivo.close()
#
#
# def ler_arquivo_product_id():
#     caminho = '../data/order_details.csv'
#     arquivo = open(caminho, "r")
#     texto_do_arquivo = arquivo.read()
#     texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#     texto_do_arquivo_organizado_mais_ainda_str = str(texto_do_arquivo_organizado)
#     texto_do_arquivo_organizado_mais_ainda = texto_do_arquivo_organizado_mais_ainda_str.split(",")
#     for x in range(1, len(texto_do_arquivo_organizado), 5):
#         print(texto_do_arquivo_organizado_mais_ainda[x])
#     arquivo.close()
#
#
# def ler_arquivo_unit_price():
#     caminho = '../data/order_details.csv'
#     arquivo = open(caminho, "r")
#     texto_do_arquivo = arquivo.read()
#     texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#     texto_do_arquivo_organizado_mais_ainda_str = str(texto_do_arquivo_organizado)
#     texto_do_arquivo_organizado_mais_ainda = texto_do_arquivo_organizado_mais_ainda_str.split(",")
#     for x in range(2, len(texto_do_arquivo_organizado), 5):
#         print(texto_do_arquivo_organizado_mais_ainda[x])
#     arquivo.close()
#
#
# def ler_arquivo_quantity():
#     caminho = '../data/order_details.csv'
#     arquivo = open(caminho, "r")
#     texto_do_arquivo = arquivo.read()
#     texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#     texto_do_arquivo_organizado = str(texto_do_arquivo_organizado).split(",")
#     for x in range(8, len(texto_do_arquivo_organizado), 5):
#         print(texto_do_arquivo_organizado[x])
#     arquivo.close()
#
#
# def ler_arquivo_discount():
#     caminho = '../data/order_details.csv'
#     arquivo = open(caminho, "r")
#     texto_do_arquivo = arquivo.read()
#     texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#     texto_do_arquivo_organizado = str(texto_do_arquivo_organizado).split(",")
#     palavra_1 = ''
#     for x in range(9, len(texto_do_arquivo_organizado), 5):
#         texto = texto_do_arquivo_organizado[x]
#         palavra_1 += f'{texto}\n'
#         palavra_2 = "['"
#         for letra in palavra_2:
#             if letra in palavra_1:
#                 palavra_1 = palavra_1.replace(letra, '')
#     arquivo.close()
#     return palavra_1

# class Arquivo:
#     def __init__(self):
#         pass
#
#     def ler_arquivo_inteiro(self):
#         caminho = "C:/Users/Usuario/Desktop/Teste pratico indicium/code-challenge/data/order_details.csv"
#         arquivo = open(caminho, "r")
#         texto_do_arquivo = arquivo.read()
#         texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#         print(texto_do_arquivo_organizado[0])
#         for x in range(1, len(texto_do_arquivo_organizado)):
#             print(texto_do_arquivo_organizado[x])
#         arquivo.close()
#
#     def ler_arquivo_order_id(self):
#         caminho = "C:/Users/Usuario/Desktop/Teste pratico indicium/code-challenge/data/order_details.csv"
#         arquivo = open(caminho, "r")
#         texto_do_arquivo = arquivo.read()
#         texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#         texto_do_arquivo_organizado_mais_ainda_str = str(texto_do_arquivo_organizado)
#         texto_do_arquivo_organizado_mais_ainda = texto_do_arquivo_organizado_mais_ainda_str.split(",")
#         for x in range(0, len(texto_do_arquivo_organizado), 5):
#             print(texto_do_arquivo_organizado_mais_ainda[x])
#         arquivo.close()
#
#     def ler_arquivo_product_id(self):
#         caminho = "C:/Users/Usuario/Desktop/Teste pratico indicium/code-challenge/data/order_details.csv"
#         arquivo = open(caminho, "r")
#         texto_do_arquivo = arquivo.read()
#         texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#         texto_do_arquivo_organizado_mais_ainda_str = str(texto_do_arquivo_organizado)
#         texto_do_arquivo_organizado_mais_ainda = texto_do_arquivo_organizado_mais_ainda_str.split(",")
#         for x in range(1, len(texto_do_arquivo_organizado), 5):
#             print(texto_do_arquivo_organizado_mais_ainda[x])
#         arquivo.close()
#
#     def ler_arquivo_unit_price(self):
#         caminho = "C:/Users/Usuario/Desktop/Teste pratico indicium/code-challenge/data/order_details.csv"
#         arquivo = open(caminho, "r")
#         texto_do_arquivo = arquivo.read()
#         texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#         texto_do_arquivo_organizado_mais_ainda_str = str(texto_do_arquivo_organizado)
#         texto_do_arquivo_organizado_mais_ainda = texto_do_arquivo_organizado_mais_ainda_str.split(",")
#         for x in range(2, len(texto_do_arquivo_organizado), 5):
#             print(texto_do_arquivo_organizado_mais_ainda[x])
#         arquivo.close()
#
#     def ler_arquivo_quantity(self):
#         caminho = "C:/Users/Usuario/Desktop/Teste pratico indicium/code-challenge/data/order_details.csv"
#         arquivo = open(caminho, "r")
#         texto_do_arquivo = arquivo.read()
#         texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#         texto_do_arquivo_organizado_mais_ainda_str = str(texto_do_arquivo_organizado)
#         texto_do_arquivo_organizado_mais_ainda = texto_do_arquivo_organizado_mais_ainda_str.split(",")
#         for x in range(3, len(texto_do_arquivo_organizado), 5):
#             print(texto_do_arquivo_organizado_mais_ainda[x])
#         arquivo.close()
#
#     def ler_arquivo_discount(self):
#         caminho = "C:/Users/Usuario/Desktop/Teste pratico indicium/code-challenge/data/order_details.csv"
#         arquivo = open(caminho, "r")
#         texto_do_arquivo = arquivo.read()
#         texto_do_arquivo_organizado = texto_do_arquivo.split("\n")
#         texto_do_arquivo_organizado_mais_ainda_str = str(texto_do_arquivo_organizado)
#         texto_do_arquivo_organizado_mais_ainda = texto_do_arquivo_organizado_mais_ainda_str.split(",")
#         for x in range(4, len(texto_do_arquivo_organizado), 5):
#             print(texto_do_arquivo_organizado_mais_ainda[x])
#         arquivo.close()
#
#
# if __name__ == "__main__"
#     arquivo = Arquivo()
#     # print(arquivo.ler_arquivo_inteiro())
#     # print(arquivo.ler_arquivo_order_id())
#     # print(arquivo.ler_arquivo_product_id())
#     # print(arquivo.ler_arquivo_unit_price())
#     # print(arquivo.ler_arquivo_quantity())
#     # print(arquivo.ler_arquivo_discount())