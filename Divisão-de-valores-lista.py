valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')