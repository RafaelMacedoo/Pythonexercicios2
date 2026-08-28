from datetime import datetime
dd = dict()

dd['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dd['Idade'] = datetime.now().year - nascimento
dd['Ctps'] = int(input('Ctps (0 não tem): '))
if dd['Ctps'] != 0:
    dd['Contratação'] = int(input('Ano de contratação: '))
    dd['Salário'] = float(input('Salário: '))
    dd['Aposentadoria'] = dd['Idade'] + ((dd['Contratação'] + 35) - datetime.now().year)

print('=-' * 20)

for k,v in dd.items():
    print(f' - {k} tem o valor {v}')