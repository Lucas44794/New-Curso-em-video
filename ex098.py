from time import sleep
def linha():
    print('-=' * 40)

def contador(inicio, fim, passo):
    if passo != 0:
        if inicio < fim:
            print(f'Contando de {inicio} a {fim} indo de {passo} em {passo}')
            for i in range(inicio, fim + 1, passo):
                print(f'{i}',end=' ')
                sleep(0.5)
        if inicio > fim:
            if passo < 0:
                print(f'Contando de {inicio} a {fim} indo de {passo} em {passo}')
                for i in range(inicio, fim-1, passo):
                    print(f'{i}',end=' ')
                    sleep(0.5)
            else:
                print(f'Contando de {inicio} a {fim} indo de -{passo} em -{passo}')
                for i in range(inicio, fim-1, -passo):
                    print(f'{i}',end=' ')
                    sleep(0.5)
        if inicio == fim:
            print('Valor incorreto inserido')
        print('FIM')
    else:
        print('Passo 0 não existe!')



print('~' * 40)
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
ini = int(input('Inicio: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
print('~' * 40)
sleep(1)
contador(ini, fi, pas)
