
import os
import json

vermelho = "\033[31m"
branco = "\033[0m"
verde = "\033[32m"

def ler_lista():
    try:
        with open('lista.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_lista(lista):
    with open('lista.json', 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

# comandos
def listar():
    lista = ler_lista()
    print('lista de tarefas:')
    print()
    for tarefa in lista:
        print(tarefa)
    print()

def apagar():
    lista = ler_lista()
    if not lista:
        print(f'{vermelho}Nenhuma tarefa para apagar!{branco}')
        return None
    deletado = lista.pop()
    salvar_lista(lista)
    return deletado

def refazer(argumento_deletado):
    lista = ler_lista()
    if argumento_deletado is not None:
        lista.append(argumento_deletado)
        salvar_lista(lista)

# sistema
deletado = None
while True:
    print('comandos: listar apagar refazer')
    opcao = input('Digite uma tarefa ou comando: ').lower()
    if opcao == 'listar':
        os.system('cls')
        listar()
    elif opcao == 'apagar':
        os.system('cls')
        deletado = apagar()
        if deletado is not None:
            print(f'{verde}Tarefa apagada com sucesso!{branco}')
    elif opcao == 'refazer':
        os.system('cls')
        if deletado is not None:
            refazer(argumento_deletado=deletado)
            print(f'{verde}Tarefa refeita com sucesso!{branco}')
            deletado = None
        else:
            print(f'{vermelho}Nenhuma tarefa para refazer!{branco}')
    elif opcao == 'sair':
        os.system('cls')
        print(f'{verde}Até mais!{branco}')
        break
    else:
        lista = ler_lista()
        lista.append(opcao)
        salvar_lista(lista)
        os.system('cls')
        print(f'{verde}Tarefa adicionada com sucesso!{branco}')