def maior(* x):
    if x != ' ':
        lista = list()
        for i in x:
            lista.append(i)
        lista.sort(reverse=True)
        print(f'Foram informados {len(lista)} valores.')
        print(f'O maior valor informado foi {lista[0]}.')
        print('-=' * 40)
        lista.clear()
    else:
        lista.append('0')
        print('Foram informados 0 valores.')
        print('O maior valor informado foi 0.')
        print('-=' * 40)
        lista.clear()

maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior('')
