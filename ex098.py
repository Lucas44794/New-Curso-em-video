def contador(inicio, fim, passo):
    for i in range(1, 11, 1):
        print(f'{i}',end=' ')
    print()
    for i in range(10,-1,-1):
        print(f'{i}',end=' ')
    print()
    if passo != 0:
        if inicio < fim:
            for i in range(inicio, fim + 1, passo):
                print(f'{i}',end=' ')
        print()
        if inicio > fim:
            for i in range(fim, inicio+1, -passo):
                print(f'{i}',end=' ')
        if inicio == fim:
            print('Valor incorreto inserido')
    else:
        print('Passo 0 não existe!')



print('~' * 30)
ini = int(input('Inicio: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
print('~' * 30)
contador(ini, fi, pas)