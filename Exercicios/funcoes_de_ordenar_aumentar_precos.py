import copy
def aumentar_preco_porcentual(produtos: list, percentual: float = 0) -> list:
    produtos = copy.deepcopy(produtos)
    porcentagem = 1 + (percentual / 100)
    for produto in produtos:
        produto['preco'] = round((produto['preco'] * porcentagem), 1)
    return produtos

def ordenar_decrescente_nome(produtos: list) -> list:
    produtos = copy.deepcopy(produtos)
    lista = sorted(produtos, key=lambda x: x['nome'], reverse=True)
    return lista

def ordenar_crescente_preco(produtos: list) -> list:
    produtos = copy.deepcopy(produtos)
    lista = sorted(produtos, key=lambda x: x['preco'])
    return lista
