'''Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''

class Quadrado:
    
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado
        
    def mudarValorLado(self, lado):
        self.tamanhoLado = lado
        
    def retornarValorLado(self):
        print(f"O valor do lado é {self.tamanhoLado}")
        
    def Area(self):
        print(f'A área do quadrado é igual a {self.tamanhoLado * self.tamanhoLado}')
        
quadradin = Quadrado(4)
quadradin.retornarValorLado()
quadradin.mudarValorLado(7)
quadradin.retornarValorLado()
quadradin.Area()
