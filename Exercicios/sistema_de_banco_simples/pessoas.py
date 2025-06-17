from contas import ContaCorrente, ContaPoupanca
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade
    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade

    def __str__(self) -> str:
        nome_da_classe = self.__class__.__name__
        return f'{nome_da_classe}\n Nome: {self._nome}\nIdade: {self._idade}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: ContaCorrente | ContaPoupanca | None = None) -> None:
        super().__init__(nome, idade)
        self.conta = conta

    def __str__(self) -> str:
        nome_da_classe = self.__class__.__name__
        return f'{nome_da_classe}\nNome: {self._nome}\nIdade: {self._idade}\nConta: {self.conta}'
    
 