class Conta:
    
    def __init__(self, numero, titular, saldo, limite = 1000): # self é a referência do objeto (qual objeto está sendo construido)
        print(f"Construindo um objeto... {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print(f"O Saldo do titular {self.titular} é de R${self.saldo}")
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"O valor de R${valor} foi depositado a sua conta!")
        
    def sacar(self, valor):
        self.saldo -= valor
        print(f"O valor de R${valor} foi retirado da sua conta")