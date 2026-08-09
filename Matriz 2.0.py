matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sopar = maior = socol = 0
for l in range(0,3):
    for c in range (0,3):
        matriz [c][l] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sopar += matriz[l][c]
    print()
print('=-' * 20)
print(f'A soma dos valores pares é {sopar}.')
for l in range(0, 3):
    socol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {socol}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')