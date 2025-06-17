from contas import ContaPoupanca
from pessoas import Cliente, Pessoa

pessoa1 = Cliente('João', 20, ContaPoupanca('123', 1000, 'poupanca'))

print(pessoa1)
