import random
sorteados = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'Os números sorteados foram: {sorteados}')
print(f'O maior valor sorteado foi {max(sorteados)}')
print(f'O menor valor sorteado foi {min(sorteados)}')