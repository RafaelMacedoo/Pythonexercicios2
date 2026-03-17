import random
vit = 0
while True:
    valor = int(input('Digite um valor: '))
    while True:
        escolha = str(input('Quer Par ou Ímpar? [P/I] ')).strip().upper()[0]
        if escolha not in 'PI':
            print('Escolha Inválida! Escolha Par ou Ímpar')
            continue
        break
    print('-' * 65)
    pc = random.randint(0, 10)
    s = valor + pc
    if s % 2 == 0:
        resultado = 'P'
        print(f'Você jogou {valor} e o computador jogou {pc}, totalizando {s}, deu par.')
    else:
        resultado = 'I'
        print(f'Você jogou {valor} e o computador jogou {pc}, totalizando {s}, deu ímpar.')
    print('-' * 65)
    if escolha == resultado:
        vit += 1
        print('Você venceu!')
        print('Vamos jogar novamente!')
    else:
        print('Você perdeu!')
        print(f'Você ganhou {vit} vezes.')
        break
    print('-' * 30)