palavra_secreta= "python"

nova_palavra_secreta = ""
for letra in palavra_secreta:
    nova_palavra_secreta += '*' 
tentativas = 0

vermelho = "\033[31m"
verde = "\033[32m"
branco = "\033[0m"
import os

print("Bem-vindo ao jogo da Forca!")

while True:
    letra = input('digite uma letra: ').lower()
    try:
        if len(letra) != 1:
            raise ValueError("Por favor, digite apenas uma letra.")
        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    nova_palavra_secreta = list(nova_palavra_secreta)
                    nova_palavra_secreta[i] = letra
                    nova_palavra_secreta = ''.join(nova_palavra_secreta)
            print(f'{verde} parabéns, você acertou uma letra!{branco}')
        print(f'Palavra: {nova_palavra_secreta}')
        tentativas += 1
        if nova_palavra_secreta == palavra_secreta:
            os.system('clear')
            print(f'{verde} Parabéns, você ganhou! A palavra era: {palavra_secreta.upper()} {branco}')
            print(f'Quantidade de tentativas: {tentativas}')
            break
    except ValueError as e:
        print(f'{vermelho} Erro: {e} {branco}')
        tentativas += 1
            
