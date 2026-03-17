'''valores = list()

for num in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
valores.sort()
for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}!')
print('Cheguei ao final da lista !')'''

a = [2, 3, 5, 7]
b = a[:] #isso faz uma copia dos itens de A para B, podendo alterar b e a livremente sem se alterarem
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')