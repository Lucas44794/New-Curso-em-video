from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Análisando os valores passados',end='')
    for i in range(0,2):
        print('.',end='')
    print()
    for valor in num:
        print(f'{valor} ',end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram Informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()