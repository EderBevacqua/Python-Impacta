import math


class Ponto():
    '''
    Implementa a abstração de um ponto no plano Cartesiano 2D,
    que possui como atributos as coordenadas x e y
    '''

    def __init__(self, x: float, y: float) -> None:
        '''
        Construtor da classe
        '''
        self.x = x
        self.y = y

    def desloca(self, dx: float, dy: float) -> None:
        '''
        Desloca o ponto em dx no eixo x e dy no eixo y
        '''
        self.x += dx
        self.y += dy

    def distancia(self, ponto: 'Ponto') -> float:
        '''
        Calcula a distância euclidiana em relação a outro ponto
        passado como argumento
        '''
        d2 = (self.x - ponto.x)**2 + (self.y - ponto.y)**2
        return math.sqrt(d2)

    