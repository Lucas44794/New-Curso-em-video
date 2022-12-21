time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gold na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: '))[0]
        if resp in 'SsNn':
            break
        print('Erro! Responda somente s ou n')
    if resp in 'Nn':
        break
print('-=' * 40)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! não existe jogador com o código {busca}!')
    else:
        print(f'  --  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-' * 40)