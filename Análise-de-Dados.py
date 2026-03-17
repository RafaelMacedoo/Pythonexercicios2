maior18 = 0
h = 0
mulheres20 = 0
while True:
    print('-' * 30)
    print(f'CADASTRO DE DADOS')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior18 += 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()[0]
        if sexo not in 'MF':
            continue
        break
    if sexo == 'M':
        h += 1
    elif sexo == 'F' and idade < 20:
        mulheres20 += 1
    print('-' *30)
    while True:
        continuar = str(input('Deseja continuar? ')).upper()[0]
        if continuar not in 'SN':
            continue
        break
    if continuar == 'S':
        continue
    else:
        print('-' * 30)
        print(f'O total de pessoas com mais de 18 anos é {maior18}.')
        print(f'O total de homens cadastrados foi de {h}')
        print(f'A quantidade de mulheres com menos de 20 anos é de {mulheres20}')
        break
