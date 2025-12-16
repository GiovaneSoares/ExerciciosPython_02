"""Exercício 10.

Crie uma classe chamada ContaBancaria para representar uma conta bancária básica.
Esta conta deve conter um número de conta, o nome do titular da conta e o saldo
disponível.
Implemente os seguinte método mágico:
    __str__(self): Retorna uma representação em formato de string da conta no seguinte
    formato: Conta: [número] de [titular]: R$ [saldo].
Além dos métodos mágicos, implemente também os seguintes métodos:
    depositar(self, valor): Adiciona um determinado valor ao saldo da conta.
    sacar(self, valor): Retira um valor específico do saldo da conta, desde que haja
    saldo suficiente.
"""
class ContaBancaria:
    def __init__(self, numero_conta: int, titular: str, saldo:float) -> None:
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo =  saldo

    def __str__(self) -> str:
        return f"Conta: {self.numero_conta}\nTitular: {self.titular}\nSaldo R$ {self.saldo:.2f}"
    
    def depositar(self, valor: float):
        if valor <= 0:
            print("O valor de deposito deve ser superior a zero!")
        
        elif valor > 0:
            self.saldo += valor
            print(f"Deposito: R${valor} realizado.\nNovo Saldo R${self.saldo:.2f}")

    def sacar(self, valor: float):
        if valor <= 0:
            print("O valor de saque deve ser positivo.")

        if self.saldo < valor:
            print(f"Saldo insuficiente. O valor de saque (R${valor}) é maior do que o saldo atual (R${self.saldo:.2f}).")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
            print(f"Novo saldo R${self.saldo:.2f}")
        
giovane = ContaBancaria(10101, "Giovane", 500)
giovane.sacar(600)