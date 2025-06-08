import os

vermelho = "\033[31m"
branco = "\033[0m"
verde = "\033[32m"

lista = []

while True:
    print('selecione uma opção')
    print('[I]nserir [A]pagar [L]istar [S]air') 
    opcao = input('Opção: ').upper()

    try:
        if opcao == 'I':

            os.system('cls')
            item = input('insira um Item: ')
            os.system('cls')
            lista.append(item)

            print(f'{verde}Item inserido com sucesso!{branco}')
            continue
        
        elif opcao == 'A':

            os.system('cls')
            indice = int(input('Digite o indice do item que deseja apagar: '))

            if indice <= (len(lista) -1):
                os.system('cls')
                del lista[indice]
                print(f'{verde}Item apagado com sucesso!{branco}')

            elif indice > (len(lista) -1):
                raise ValueError
            
            else:
                raise ValueError
            
        elif opcao == 'L':
            os.system('cls')

            if len(lista) > 0:
                for indice, item in enumerate(lista):
                    print(indice, item)

            else:
                print(f'{vermelho}Nenhum item cadastrado.{branco}')
                continue

        elif opcao == 'S':
            os.system('cls')
            print(f'{verde}Obrigado por usar nosso programa!{branco}')
            break

        else:
            raise ValueError
        
    except:
        print(f'{vermelho}Opção inválida!{branco}')