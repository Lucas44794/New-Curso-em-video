jogador = dict()
gol = list()
total = 0
jogador['Nome'] = str(input('Nome do Jogador: '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? : '))
if jogador["Partidas"] == 0:
    print('Até a proxima')
else:
    for i in range(1, jogador["Partidas"]+ 1):
        gol.append(int(input(f'Quantos gols o jogador fez na {i}º partida? ')))
        total += gol[i - 1]
    jogador['Gols'] = gol[:]
    jogador['Total'] = total
print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, i in jogador.items():
    print(f'O campo {k} tem o valor {i}.')
print('-=' * 40)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for k, i in enumerate(jogador["Gols"]):
    print(f'       => Na partida {k+1}, fez {i} gols ')
print(f'Foi um total de {total} Gols')
