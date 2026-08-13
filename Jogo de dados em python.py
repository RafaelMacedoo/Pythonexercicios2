import random
import operator
from time import sleep

jogadores = dict()
jogadores['jogador1'] = random.randint(1, 6)
jogadores['jogador2'] = random.randint(1, 6)
jogadores['jogador3'] = random.randint(1, 6)
jogadores['jogador4'] = random.randint(1, 6)

for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('=-' * 20)
ranking = list()
ranking = sorted(jogadores.items(), key = operator.itemgetter(1), reverse = True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
