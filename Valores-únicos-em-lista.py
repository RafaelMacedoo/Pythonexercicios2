valores = list()
opcao = ' '
while True:
    if opcao == 'N':
        break
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        print('Valor adicionado com sucesso.')
        valores.append(valor)
        print('=-' * 15)
    else:
        print('Valor duplicado. Não será adicionado.')

    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    print('=-' * 15)
    if opcao == 'S':
        continue
    if opcao == 'N':
        break
    while True:
        if opcao not in 'SN':
            print('Resposta inválida!')
            opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
            print('=-' * 15)
        else:
            break
print(f'Você digitou os valores {sorted(valores)}')