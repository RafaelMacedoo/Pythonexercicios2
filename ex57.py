'''sex = ' '
while sex not in 'MF':
    sex = str(input('Me diga o seu sexo: ')).upper().strip()[0]
    if sex == 'M':
        print('Sexo masculino registrado!')
    if sex == 'F':
        print('Sexo feminino registrado!')
    if sex not in 'MF':
        print('-'* 55)
        print('Sua resposta não faz sentido, responda corretamente.')
        print('-' * 55)'''

sex = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sex not in "MF":
    sex = str(input('Dados inválidos. Informe seu sexo: [M/F] ')).upper().strip()[0]
print('Sexo registrado!')