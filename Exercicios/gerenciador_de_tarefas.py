
import os
import json

vermelho = "\033[31m"
branco = "\033[0m"
verde = "\033[32m"
azul = "\033[34m"

#funções

def ler_lista():
    try:
        with open('lista.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f'{vermelho}Nenhuma tarefa para listar!, adicione uma tarefa primeiro.{branco}')
        return 

def salvar_lista(lista):
    with open('lista.json', 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

# comandos
def listar(lista):
    os.system('cls')
    if lista:
        print(f'{azul}lista de tarefas:{branco}')
        print()
        for tarefa in lista:
            print(tarefa)
        print()
        return
    print(f'{vermelho}Nenhuma tarefa para listar!{branco}')
    print()
    return

def apagar(lista, argumento_deletado):
    os.system('cls')
    if not lista:
        print(f'{vermelho}Nenhuma tarefa para apagar!{branco}')
        return None
    tarefa = lista.pop()
    argumento_deletado.append(tarefa)
    salvar_lista(lista)
    print(f'{verde}Tarefa apagada com sucesso!{branco}')
    print()
    return

def refazer(lista, argumento_deletado):
    os.system('cls')
    if argumento_deletado is not None:
        tarefa = argumento_deletado.pop()
        lista.append(tarefa)
        salvar_lista(lista)
        print(f'{verde}Tarefa refeita com sucesso!{branco}')
        print()
        return
    
    print(f'{vermelho}Nenhuma tarefa para refazer!{branco}')
    return

def sair():
    print(f'{vermelho}Saindo...{branco}')
    os._exit(0)
    
argumento_deletado =[]
# sistema


comandos = {
    'listar': lambda: listar(lista),
    'apagar': lambda: apagar(lista, argumento_deletado),
    'refazer': lambda: refazer(lista, argumento_deletado),
    'sair': lambda: sair()
}

while True:
    lista = ler_lista()
    print('Comandos: Listar, Apagar, Refazer')
    resposta = input('Digite um comando ou uma tarefa: ').lower()

    if resposta in comandos:
        comandos[resposta]()
    else:
        lista = ler_lista()
        lista.append(resposta)
        salvar_lista(lista)
        os.system('cls')
        print(f'{verde}Tarefa adicionada com sucesso!{branco}')
        print()
    
    