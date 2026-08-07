grupo = []
temp = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    grupo.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp =='N':
        break

print(f'No final tiveram {len(grupo)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
