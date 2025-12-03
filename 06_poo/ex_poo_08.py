"""Exercício 08.

Crie uma classe ContaBancaria que represente uma conta bancária básica.
Utilize os conceitos de encapsulamento para proteger os atributos relacionados ao saldo
e ao titular da conta.
Implemente métodos para movimentar o saldo, como depósito e saque, garantindo que sejam
realizados de forma segura e controlada.
Além disso, forneça um método para trocar o titular da conta, mantendo a integridade
dos dados.
Certifique-se de que todas as operações sejam realizadas de acordo com as regras
estabelecidas pelo banco e que os atributos sensíveis estejam acessíveis apenas por
métodos apropriados.
"""
from decimal import Decimal

class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.__titular: str = titular
        self.__saldo: Decimal = Decimal(str(saldo))

    def get_saldo(self) -> Decimal:
        return self.__saldo
    
    def get_titular(self) -> str:
        return self.__titular
    
    def set_titular(self, novo_titular: str):
        if novo_titular:
            self.__titular = novo_titular
            return f"Titular da conta alterado para {self.__titular}."
        return "O nome do titular não pode estár em branco."
    
    def get_info(self):
        return f"Titular: {self.__titular}\nSaldo: R$ {self.__saldo:.2f}"
    
    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += Decimal(valor)
            return f"Deposito de R$ {valor:.2f} realizado."
        
        elif valor <= 0:
            return "O valor para deposito tem que ser maior que zero."
        
        return "Deposito invalido!"
        
    def sacar(self, valor: float):
        if valor > 0:
            self.__saldo -= Decimal(valor)
            return f"Saque de R$ {valor:.2f} realizado."
        
        elif valor <= 0:
            return f"O valor para saque tem que ser maior que zero."
        
        return "Saque invalido!"
    
conta = ContaBancaria("Giovane", 500)

print(conta.depositar(100))
print(conta.sacar(150))
print(conta.get_info())
print(conta.get_saldo())
print(conta.get_titular())
