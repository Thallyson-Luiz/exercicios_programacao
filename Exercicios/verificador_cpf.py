import os
vermelho = "\033[31m"
verde = "\033[32m"
branco = "\033[0m"

while True:
    cpf = input('Digite seu CPF: ')
    cpf = cpf.replace(' ', '')
    try:
        if len(cpf) != 11:
            raise ValueError
        cpf = int(cpf)
    except:
        try:
            primeiros_numeros_cpf, ultimosNumeros_cpf = cpf.split('-')
            primeiros_numeros_cpf = primeiros_numeros_cpf.split('.')
            primeiros_numeros_CPF = []
            ultimosNumerosCPF = []

            for numeros in primeiros_numeros_cpf:
                if len(numeros) == 3:
                    numeros = list(numeros)
                    for n in numeros:
                        if n.isnumeric():
                            n = int(n)
                            primeiros_numeros_CPF.append(n)
                else:
                    raise ValueError
            
            if len(ultimosNumeros_cpf) == 2:
                ultimosNumeros_cpf = list(ultimosNumeros_cpf)
                for numeros in ultimosNumeros_cpf:
                    if numeros.isnumeric():
                        numeros = int(numeros)
                        ultimosNumerosCPF.append(numeros)
            else:
                raise ValueError

        except:
            os.system('cls')
            print(f'{vermelho}erro: CPF False!{branco}')
            continue

        try:
            if len(primeiros_numeros_CPF) != 9 or len(ultimosNumerosCPF) != 2:
                raise ValueError
        except:
            os.system('cls')
            print(f'{vermelho}erro: tamanho do CPF!{branco}')
            continue
        
        cpf = ''
        for numero in primeiros_numeros_CPF:
            cpf += str(numero)
        for numero in ultimosNumerosCPF:
            cpf += str(numero)

    cpf = str(cpf)
    cpf = list(cpf)
    try:
        cpf_numeros_repetidos = cpf == [cpf[0]] * len(cpf)
        if cpf_numeros_repetidos:
            raise ValueError
    except:
        os.system('cls')
        print(f'{vermelho}erro: CPF com muitos numeros repetidos!{branco}')
        continue

    contador = 10
    total_soma_cpf = 0
    for indice, numero in enumerate(cpf):
        if indice > 8:
            break
        else:
            numero = int(numero)
            total_soma_cpf += numero * contador
            contador -= 1

    total_soma_cpf *= 10
    total_soma_cpf = total_soma_cpf % 11
    

    if total_soma_cpf > 9:
        total_soma_cpf = 0

    total_soma_cpf_digito2 = 0
    contador = 11
    for indice, numero in enumerate(cpf):
        if indice > 9:
            break
        else:
            numero = int(numero)
            total_soma_cpf_digito2 += numero * contador
            contador -= 1

    total_soma_cpf_digito2 *= 10
    total_soma_cpf_digito2 = total_soma_cpf_digito2 % 11

    if total_soma_cpf_digito2 > 9:
        total_soma_cpf_digito2 = 0
    
    resultado_do_calculo = str(total_soma_cpf) + str(total_soma_cpf_digito2)

    if resultado_do_calculo == ''.join(cpf[-2:]):
        os.system('cls')
        print(f'{verde}CPF Valido!{branco}')
    else:
        os.system('cls')
        print(f'{vermelho}CPF Inválido ou nao existente!{branco}')
