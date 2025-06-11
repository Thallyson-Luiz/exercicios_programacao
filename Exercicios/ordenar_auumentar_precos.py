from funcoes_de_ordenar_aumentar_precos import *

produtos = [
    {'nome': 'Notebook', 'preco': 2500.00},
    {'nome': 'Celular', 'preco': 1500.00},
    {'nome': 'Tablet', 'preco': 1000.00},
    {'nome': 'Monitor', 'preco': 800.00},
    {'nome': 'Teclado', 'preco': 200.00},
    {'nome': 'Mouse', 'preco': 100.00},
    {'nome': 'Impressora', 'preco': 600.00},
    {'nome': 'Cadeira Gamer', 'preco': 1200.00},
    {'nome': 'Webcam', 'preco': 300.00},
    {'nome': 'Fone de Ouvido', 'preco': 400.00}
]


for n in ordenar_decrescente_nome(produtos=produtos):
    print(n)
print()
for n in aumentar_preco_porcentual(produtos=produtos, percentual=10):
    print(n)
print()
for n in ordenar_crescente_preco(produtos=produtos):
    print(n)
