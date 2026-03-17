sex = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sex not in "MF":
    sex = str(input('Dados inválidos. Informe seu sexo: [M/F] ')).upper().strip()[0]
print('Sexo registrado!')
