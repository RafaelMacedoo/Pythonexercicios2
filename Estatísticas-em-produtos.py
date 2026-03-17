totgasto = preco = 0
caro = 0
menorp = 0
promenor = 0
cont = 0
while True:
    produto = str(input('Produto: ')).strip().capitalize()
    preco = float(input('Preço: $ '))
    totgasto += preco
    cont += 1
    if cont == 1 or preco < menorp:
        menorp = preco
        promenor = produto
    if produto and preco >= 1000:
        caro += 1
    while True:
        print('-' * 30)
        continuar = input('Deseja continuar? [Sim/Não] ').upper().strip()
        print('-' * 30)
        if continuar.startswith('S'):
            continuar = 'S'
            break
        elif continuar.startswith('N'):
            continuar = 'N'
            break
        else:
            print('Resposta inválida. Digite Sim ou Não.')
    if continuar == 'N':
        print('-' * 30)
        print(f'O total gasto na compra foi R${totgasto}')
        print(f'{caro} produtos custam mais de R$1000.00')
        print(f'{promenor} foi o produto mais barato da compra custando R${menorp:.2f}')
        break
