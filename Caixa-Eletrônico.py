ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0
valor = int(input('Informe o valor a ser sacado: '))
while True:
    if valor >= 50:
        ced50 += 1
        valor = valor - 50
    elif valor >= 20:
        ced20 += 1
        valor = valor - 20
    elif valor >= 10:
        ced10 += 1
        valor = valor - 10
    elif valor < 10 :
        ced1 += 1
        valor = valor - 1
    if valor == 0:
        print(f'Total de {ced50} cédulas de R$50')
        print(f'Total de {ced20} cédulas de R$20')
        print(f'Total de {ced10} cédulas de R$10')
        print(f'Total de {ced1} cédulas de R$1')
        break
