escola = {'Nome': '', 'Média': '', 'Situação': ''}

escola['Nome'] = str(input('Qual seu nome? '))
escola['Média'] = float(input(f"Qual a média de {escola['Nome']}? "))
print('=-' * 20)

if escola['Média'] < 4:
    escola['Situação'] = 'Reprovado'
elif escola['Média'] < 7:
    escola['Situação'] = 'Recuperação'
else:
    escola['Situação'] = 'Aprovado'

for k, v in escola.items():
    print(f' {k} é igual a {v}')