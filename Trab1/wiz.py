import sys
import math

# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle and use your team id to determine where you need to throw it.

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left


#condicao para identificar o lado que o mago tem que fazer o gol
if my_team_id == 1:
    gol = [0, 3750]              #coordenadas do centro do gol a esquerda
else:
    gol = [16000, 3750]          #coordenadas do centro do gol a direita



#classe para armazenar os dados das entidades
class Entities:
    entityType = None        #armazena o tipo de entidade (WIZARD, OPPONENT_WIZARD, SNAFFLE)
    entitiesId = None        #armazena o ID de cada entidade
    x, y = None, None        #armazena a posicao de cada entidade
    vx, vy = None, None      #armazena a velocidade da entidade
    state = None             #armazena o estado da entidade(1 se o mago estiver com a snaffle e 0 caso contrario)
    
    #contrutor para inicializar as variaveis
    def __init__(self, entity_type, entity_id, _x, _y, _vx, _vy, _state):
        self.entityType = entity_type
        self.entitiesId = entity_id
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.state = _state


#classe para identificar e armazenar os magos
class Wizard:
    x = None
    y = None
    vx = None
    vy = None
    state = None

    #construtor
    def __init__(self, entitie):
        self.x = entitie.x
        self.y = entitie.y
        self.vx = entitie.vx
        self.vy = entitie.vy
        self.state = entitie.state
    
    #metodos para chutar o snaffle e movimentar o mago
    @staticmethod
    def move(x, y, thrust):
        print('MOVE %s %s %s' % (x, y, thrust))    

    @staticmethod
    def throw(x, y, power):
        print('THROW %s %s %s' % (x, y, power))

    #metodo para calcular a distancia entre os magos e as snaffles
    def get_Distance(self, _snaffle):
        return math.sqrt((self.x - _snaffle.x)**2 + (self.y - _snaffle.y)**2)
    
    #metodo que retorna a snaffle mais proxima do mago especifico
    def get_Snaffle(self, _snaffles):
        minDist = self.get_Distance(_snaffles[0])
        snaf = None
        for snaffle in _snaffles:
            if self.get_Distance(snaffle) <= minDist:
                minDist = self.get_Distance(snaffle)
                snaf = snaffle
        
        return snaf


# game loop
while True:
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]

    entities = int(input())  #number of entities still in game

    #array para armazenar os magos
    gameWiz = []
    #array para armazenar as snaffles
    gameSnaf = []

    for i in range(entities):

        inputs = input().split()
        entity_id = int(inputs[0])  # entity identifier
        entity_type = inputs[1]  # "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
        x = int(inputs[2])  # position
        y = int(inputs[3])  # position
        vx = int(inputs[4])  # velocity
        vy = int(inputs[5])  # velocity
        state = int(inputs[6])  # 1 if the wizard is holding a Snaffle, 0 otherwise
        
        #variavel que armazena um objeto entidade
        entitie = Entities(entity_type, entity_id, x, y, vx, vy, state)
        
        #variaveis para armazenar os objetos das entidades identificadas
        wiz = None

        #condicao para adicionar os objetos das entidades nos respectivos arrays
        if entitie.entityType == 'WIZARD':
            wiz = Wizard(entitie)
            gameWiz.append(wiz)                   
        if entitie.entityType == 'SNAFFLE':
            gameSnaf.append(entitie)

    #responsavel pelo movimento do mago
    for wiz in gameWiz:
        closersnaffle = wiz.get_Snaffle(gameSnaf)             #chama a funcao getSnaffle para achar a snaffle mais proxima do mago

        if wiz.get_Distance(closersnaffle) <= 400:            #verifica se o mago esta no mesmo square do snaffle mais proximo
            wiz.throw(gol[0], gol[1], 500)                    #se estiver chuta para o centro do respectivo gol com forca maxima
        else:
            wiz.move(closersnaffle.x, closersnaffle.y, 100)   #se nao estiver faz ele mover ate o snaffle mais proximo com thruster 100
    



