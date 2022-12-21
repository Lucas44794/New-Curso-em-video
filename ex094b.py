galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip()[0]
        if pessoa['Sexo'] in 'MmFf':
            break
        else:
            print('Entrada incorreta! Tente novamente...')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja Continuar? [S/N]: '))[0]
        if resp in 'SsNn':
            break
        else:
            print('Tente novamente... responda somente S ou N')
    if resp in 'Nn':
        break
print('-=' * 40)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media das idades é de {media:5.2f} anos')
print('As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ',end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('  << Encerrado >>  ')