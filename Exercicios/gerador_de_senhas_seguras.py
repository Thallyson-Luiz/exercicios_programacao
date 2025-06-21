'''gerador de senhas completamente aleatórias'''
import secrets
import string as s
import random

# personalizavel
tamanho_da_senha = 10

def gerar_senha():
    random = secrets.SystemRandom()
    senha = ''.join(secrets.SystemRandom().choices(s.digits + s.ascii_letters + s.punctuation, k=tamanho_da_senha))
    print()
    print('Senha gerada:', senha)
    print()


gerar_senha()