c = (int(input(f'Digite um número: ')), int(input(f'Digite mais um número: ')),
     int(input(f'Digite outro número: ')), int(input(f'Digite mais um número: ')))
print(f'Você digitou os valores: {c}')
print(f'O valor 9 apareceu {c.count(9)} vezes.')
if 3 in c:
    print(f'O valor 3 apareceu na {c.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares encontrados foram: ', end='')
for n in c:
    if n % 2 == 0:
        print(n, end=' ')
