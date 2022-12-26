numeros = []
def sorteia():
    from random import randint
    for i in range(0,5):
        temp = randint(1,10)
        numeros.append(temp)
    print('Os numeros sorteados foram: ')
    for v in numeros:
        print(f'{v}',end=' ')
    print()

def somaPar(x):
    somados = 0
    for i in x:
        if i % 2 == 0:
            somados += i
    print(f'A soma dos números pares sorteados foi {somados}.')

sorteia()
somaPar(numeros)