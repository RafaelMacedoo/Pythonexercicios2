n = 0
while True:
    n = int(input('De qual número você quer a tabuada? '))
    print('-' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        m = n * c
        print(f'{n} x {c} = {m}')
    print('-' * 20)
print('Programa encerrado!')