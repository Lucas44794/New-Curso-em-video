from time import sleep
pessoa = dict()
acimaDaMedia = list()
mulheres = list()
cont = idade = idades = 0
while True:
    cont += 1
    pessoa['Nome'] = str(input('Nome: ')).strip()
    sexo = str(input('Sexo [M/F]: '))[0]
    while sexo not in 'FfMm':
        sleep(1)
        print('Valor incorreto inserido... tente novamente!')
        sexo = str(input('Sexo [M/F]: '))[0]
    pessoa['Sexo'] = sexo
    idade = int(input('Idade: '))
    pessoa['Idade'] = idade
    idades += idade
    if pessoa["Sexo"] in 'Ff':
        mulheres.append([pessoa["Nome"], pessoa["Idade"]])
    resp = str(input('Deseja Continuar? [S/N]: ')).strip()[0]
    while resp not in 'SsNn':
        sleep(1)
        print('Tente novamente!')
        resp = str(input('Deseja Continuar? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
media = int(idades / cont)
print('-=' * 40)
print(f'Foram cadastradas {cont} pessoas.')
print(f'A média das idades foi {media} anos.')
if len(mulheres) > 0:
    print('As mulheres cadastradas foram:')
    print(mulheres)
for i in range(1, len(pessoa)+ 1):
    if pessoa["Idade"] > media:
        acimaDaMedia.append([pessoa["Idade"]])
print('Fim')