info = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    resp = input('Quer conitnuar [S/N]? ').upper().strip()
    info.append([nome, [nota1, nota2], media])
    if resp == 'N':
        break
print('-'*30)
print(f'{'N°':<4}{'Nome':<8}{'Média':>5}')
for i, a in enumerate(info):
    print(f'{i:<4}{a[0]:<8}{a[2]:>5.1f}')
while True:
    print('-' * 30)
    notaa = int(input('De qual aluno você quer ver a nota? [00 Finaliza]: '))
    if notaa == 0:
        print('Finalizado')
        break
    if notaa <= len(info) - 1:
        print(f'Nota de {info[notaa][0]} são {info[notaa][1]}')