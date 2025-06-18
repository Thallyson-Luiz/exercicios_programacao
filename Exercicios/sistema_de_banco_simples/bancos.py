""" Classes e módulos para o sistema de bancos"""
from pessoas import Cliente
from contas import ContaCorrente, ContaPoupanca

class Banco:
    def __init__(
            self,
            nome: str,
            agencias: list[int] | None = None,
            clientes: list[Cliente] | None = None,
            contas: list[ContaCorrente | ContaPoupanca] | None = None
    ) -> None:
        self._nome = nome
        self._agencias = agencias or []
        self._clientes = clientes or []
        self._contas = contas or []

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def agencias(self) -> list[int]:
        return self._agencias
    
    @property
    def clientes(self) -> list[Cliente]:
        return self._clientes
    
    @property
    def contas(self) -> list[ContaCorrente | ContaPoupanca]:
        return self._contas
    
    def __str__(self) -> str:
        return f'Nome: {self._nome}\nAgencias: {self._agencias}\nClientes: {self._clientes}\nContas: {self._contas}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def _checar_cliente(self, cliente: Cliente) -> bool:
        if cliente not in self._clientes:
            print('Cliente não encontrado')
            return False
        return True
    
    def _checar_conta(self, conta: ContaCorrente | ContaPoupanca) -> bool:
        if conta not in self._contas:
            print('Conta não encontrada')
            return False
        return True
    
    def _checar_agencia(self, agencia: int) -> bool:
        if agencia not in self._agencias:
            print('Agência não encontrada')
            return False
        return True
    
    def authenticate(self, agencia: int, conta: ContaCorrente | ContaPoupanca, cliente: Cliente) -> bool:
         return self._checar_agencia(agencia) and self._checar_conta(conta) and self._checar_cliente(cliente)
    
    def sacar(self, valor : int | float, agencia: int, conta: ContaCorrente | ContaPoupanca, cliente: Cliente) -> bool:
        deu_certo = self.authenticate(agencia, conta, cliente)
        if deu_certo:
            conta.sacar(100)
        return deu_certo