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
        self.dx = dx
        self.dy = dy
        

    def distancia(self, ponto: 'Ponto') -> float:
        '''
        Calcula a distância euclidiana em relação a outro ponto
        passado como argumento
        '''
        d2 = (self.x - ponto.x)**2 + (self.y - ponto.y)**2
        return math.sqrt(d2)
        
       


class Reta():
    '''
    Cria a abstração de uma reta no plano cartesiano 2D e tem como atributos
    o coeficiente deincl
    '''
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def pertence(self, ponto: 'Ponto') -> bool:
        '''
        Devolve 'True se o ponto pertence a reta e 'False' caso contrário
        '''
        return ponto.y == self.a * ponto.x + self.b
        

    def eh_paralela(self, reta: 'Reta') -> bool:
        '''
        Retorna true se a reta é paralela a esta reta e 'False' caso contrário
        '''
        return self.a == reta.a
        
        
    def interseccao(self, reta: 'Reta') -> 'Ponto':
        '''
        Retorna o ponto de intersecção com a reta passada como argumento
        caso não haja intersecção retorna 'None'
        '''
        Xi = (self.b-reta.b/reta.a-self.a)
        Yi = (reta.a * ponto.Xi + self.b)
        return (Xi, Yi)
        
    def perpendicular(self, ponto: 'Ponto') -> 'Reta':
        '''
        BÔNUS:
        Cria uma reta perpencidular à esta reta que passa por ponto
        '''
        a2 = -1/self.a
        b2 = ponto.y - (self.a.ponto.x)
        return (a2 , b2)
        

reta1 = Reta(5,8)   '''teste pertence a reta false'''
reta2 = Reta(2,3)     '''teste pertence a reta True'''
reta3 = Reta(10,15) '''teste eh pararela false '''
reta4 = Reta(2,3)     '''teste eh pararela complemento''' 
reta5 = Reta(2,6)     '''teste eh pararela True'''
reta6 = Reta(5,7)     '''teste intersecçao'''
reta7 = Reta(7,9)     '''teste perpendicular'''

ponto1 = Ponto(2,7)


print("pertence",pertence(reta1))
