def fatorial(n, show = False):
    '''
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: Exibe ou não o calculo do fatorial (padrão Não)
    :return: Retorna o valor da fatorial
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(' x ',end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f

print(fatorial(5, True))
help(fatorial)