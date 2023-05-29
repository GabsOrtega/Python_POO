'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor'''

class Bola:
    
    def __init__(self, cor, circunferencia, material):
        print(f"Instanciando um objeto... {self}")
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
        print(f"A cor da sua bola é {self.cor}")
        print(f"A circunferencia é {self.circunferencia}")
        print(f"O material da bola é de {self.material}")
        
    def trocaCor(self, cor):
        self.cor = cor
    
    def mostraCor(self):
        print(f'A cor da bola é {self.cor}')
    
        
conta = Bola('Amarelo', 100, 'Borracha')
conta.trocaCor('Azul')
conta.mostraCor()