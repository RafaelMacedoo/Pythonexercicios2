dados= dict()
gols = list()

dados['Nome'] = str(input('Nome do jogador: '))
dados['Partidas'] = int(input(f'Quantidade de partidas jogadas por {dados["Nome"]}: '))
for c in range(0, dados['Partidas']):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
dados['Gols'] = gols.copy()
dados['Total'] = sum(gols)

print('=-' * 20)
print(dados)
print('=-' * 20)

for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('=-' * 20)

print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas.')
for i, v in enumerate(dados['Gols']):
    print(f' -> Na partida {i} ele fez {v} gols.')