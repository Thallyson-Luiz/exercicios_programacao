""" Main do sistema de bancos simples """
from contas import ContaPoupanca, ContaCorrente
from pessoas import Cliente, Pessoa
from bancos import Banco

# Exemplo de execução: sucesso
pessoa1  = Cliente('João', 20,)
pessoa1.conta = ContaCorrente(123, 1000, 'corrente', 1000)
banco = Banco('Banco do João', [134, 232, 123], [pessoa1], [pessoa1.conta])

banco.sacar(100, pessoa1.conta.agencia, pessoa1.conta, pessoa1)

# Exemplo de execução: falha

#pessoa1  = Cliente('João', 20,)
#pessoa1.conta = ContaCorrente(123, 1000, 'corrente', 1000)
#banco = Banco('Banco do João', [134], [pessoa1], [pessoa1.conta])

#banco.sacar(100, pessoa1.conta.agencia, pessoa1.conta, pessoa1)