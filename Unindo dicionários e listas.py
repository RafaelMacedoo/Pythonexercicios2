dados = {'Nome':' ', 'Sexo':' ', 'Idade':' '}
dados2 = list()
soma = media = 0

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = input('Sexo: ').upper().strip()
        if dados['Sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')

    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    dados2.append(dados.copy())

    resposta = input('Quer continuar? ').upper().strip()
    if resposta == 'N':
        break
    print('=-' * 20)
    while True:
        if resposta != 'N' and resposta != 'S':
            print('ERRO! Por favor, digite apenas N ou S.')
            resposta = input('Quer continuar? ').upper().strip()
        if resposta == 'S':
            break
media = soma / len(dados2)
print('=-' *30)
print(f'A) Ao todo temos {len(dados2)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.1f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for c in dados2:
    if c['Sexo'] in 'Ff':
        print(f' {c["Nome"]} ', end='')
print()
print(f'D) Lista de pessoas acima da média: ',end='')
for c in dados2:
    if c['Idade'] >= media:
        print('  ')
        for k, v in c.items():
            print(f' {k} = {v}; ', end='')
print()

print('Programa encerrado!')
