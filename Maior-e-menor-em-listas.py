valores = list()
posi_maior = list()
posi_menor = list()

for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {pos}: ')))
print('=-=-' *10)
print(f'Você digitou os valores: {valores}')
maior = max(valores)
menor = min(valores)

for posi, v in enumerate(valores):
    if v == maior:
        posi_maior.append(posi)
    if v == menor:
        posi_menor.append(posi)
print(f'O maior valor digitado foi {maior} nas posições {posi_maior}')
print(f'O menor valor digitado foi {menor} nas posições {posi_menor}')