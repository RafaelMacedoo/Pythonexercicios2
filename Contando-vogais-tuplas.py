lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
         'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
