def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.')
        if ok:
            break
    return valor

#Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar {n}')