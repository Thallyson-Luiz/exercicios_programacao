"""classes das contas"""
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, saldo, conta_tipo):
        self.agencia = agencia
        self.saldo = saldo
        if conta_tipo not in ['corrente', 'poupanca']:
            raise ValueError('Tipo de conta inválido')
        
        self.conta_tipo = conta_tipo

    def depositar(self, valor):
        self.saldo += valor

    def printar_saldo(self):
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        print('Saque realizado com sucesso')
        self.printar_saldo()
    
    def __str__(self) -> str:
        return f'Agencia: {self.agencia}\nSaldo: {self.saldo}\nConta: {self.conta_tipo}'
    
    def __repr__(self) -> str:
        return self.__str__()

class ContaPoupanca(Conta):
    def sacar(self, valor: int | float):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        
        self.saldo -= valor
        print('Saque realizado com sucesso')
        self.printar_saldo()
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}\nAgencia: {self.agencia}\nSaldo: {self.saldo}\nConta: {self.conta_tipo}'
    
class ContaCorrente(Conta):
    def __init__(self, agencia, saldo, conta_tipo, limite):
        super().__init__(agencia, saldo, conta_tipo)
        self.limite = limite
    
    def sacar(self, valor: int | float):
        saldo = self.saldo - valor
        limite = -self.limite 

        if saldo < limite:
            print('Saldo insuficiente')
            return
        
        self.saldo -= valor
        print('Saque realizado com sucesso')
        self.printar_saldo()
        print(f'Limite: {self.limite}')


 