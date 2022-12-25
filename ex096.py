def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg:.1f} x {comp:.1f} é {a:.1f}m².')

print('-=' * 30)
l = float(input('Largura (M): '))
c = float(input('Comprimento (M): '))
print('-=' * 30)
area(l, c)