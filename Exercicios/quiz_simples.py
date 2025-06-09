import os

perguntas = [
    {
        "pergunta": "Qual é a capital da França?",
        'opções': ['Paris', 'Londres', 'Berlim', 'Madri'],
        'resposta': 'Paris'
    },
    {
        "pergunta": "Qual é a capital do Brasil?",
        'opções': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador'],
        'resposta': 'Brasília'
    },
    {
        "pergunta": "Qual é a capital dos Estados Unidos?",
        'opções': ['Nova York', 'Washington, D.C.', 'Los Angeles', 'Chicago'],
        'resposta': 'Washington, D.C.'
    },
    {
        "pergunta": "Qual é a capital da Alemanha?",
        'opções': ['Berlim', 'Munique', 'Hamburgo', 'Frankfurt'],
        'resposta': 'Berlim'
    },
    {
        "pergunta": "Qual é a capital da Itália?",
        'opções': ['Nápoles', 'Milão', 'Veneza', 'Roma'],
        'resposta': 'Roma'
    }
]

vermelho = '\033[31m'
branco = '\033[0m'
verde = '\033[32m'
perguntas_corretas = 0
for pergunta in perguntas:
    print(pergunta["pergunta"])
    contador = 0
    letra = ''
    for opcao in pergunta["opções"]:
        if contador == 0:
            letra = 'A'
        elif contador == 1:
            letra = 'B'
        elif contador == 2:
            letra = 'C'
        elif contador == 3:
            letra = 'D'
        print(f'{letra}) {opcao}')
        contador += 1

    resposta_usuario = input("Digite a letra da sua resposta: ").strip().upper()
    print()

    if resposta_usuario == 'A':
        resposta_usuario = pergunta['opções'][0]
    elif resposta_usuario == 'B':
        resposta_usuario = pergunta['opções'][1]
    elif resposta_usuario == 'C':
        resposta_usuario = pergunta['opções'][2]
    elif resposta_usuario == 'D':
        resposta_usuario = pergunta['opções'][3]
    else:
        print('desculpe, opção inválida!')

    if resposta_usuario == pergunta['resposta']:
        print("Resposta correta!👍")
        perguntas_corretas += 1
    else:
        print(f"{vermelho}Resposta incorreta! A resposta correta é: {pergunta['resposta']}{branco}")
    print()

os.system('cls' if os.name == 'nt' else 'clear')
print(f"{verde}Você acertou {perguntas_corretas} de {len(perguntas)} perguntas.{branco}")
if perguntas_corretas == len(perguntas):
    print(f"{verde}PARABENS!{branco}")

